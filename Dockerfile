FROM ubuntu:20.04

RUN apt update && apt install -y curl git unzip xz-utils zip libglu1-mesa openjdk-8-jdk wget

RUN useradd -ms /bin/bash test
USER tester
WORKDIR /home/tester

# this folder will contain all the python scripts
RUN mkdir -p bin
ADD . /home/tester/bin
ENV PATH "$PATH:/home/tester/bin"

#  this folder will contain all the flutter application files from the repo
RUN mkdir -p repo
ENV PATH "$PATH:/home/tester/repo"
ENV PATH "$PATH:/home/tester/repo/scripts"
ENV PATH "$PATH:/home/tester/repo/docker_scripts"

#Flutter SDK
RUN git clone https://github.com/flutter/flutter.git -b stable --depth 1
ENV PATH "$PATH: /home/tester/flutter/bin"



# Android SDK 
RUN mkdir -p Android/sdk
ENV ANDROID_SDK_ROOT /home/tester/developer/Android/SDK
RUN mkdir -p .android && touch .android/repositories.cfg

RUN wget -O commandlinetools.zip  https://dl.google.com/android/repository/commandlinetools-linux-6858069_latest.zip 
RUN unzip commandlinetools.zip && rm commandlinetools.zip
RUN mv -v cmdline-tools/* Android/sdk/tools
RUN cd Android/sdk/tools/bin && yes | ./sdkmanager --licenses
RUN cd Android/sdk/tools/bin && ./sdkmanager "build-tools;29.0.2" "patcher;v4" "platform-tools" "platforms;android-29" "sources;android-29"
ENV PATH "$PATH:/home/tester/Android/sdk/platform-tools"
ENV PATH "$PATH:/home/tester/Android/sdk/tools/"
ENV PATH "$PATH:/home/tester/Android/sdk/tools/avdmanager"
