#############################################################
# AEYE AI Docker Cleaner
# Created By Yoonchul Chung
# Created At 2024.08.03
# Welcome to Visit Github : https://github.com/Yoonchulchung
#############################################################

#!/bin/bash

# Define an array of image names
IMAGE_NAMES=("aeye_web_front" "aeye_web_back" "tensorflow/tensorflow" "nginx" "aeye_ai" "aeye_ai_back")

# Initialize an empty variable to store image IDs
EXCLUDE_IMAGE_IDS=""

# Loop through the image names and get their IDs
for IMAGE_NAME in "${IMAGE_NAMES[@]}"; do
    IMAGE_ID=$(docker images -q $IMAGE_NAME)
    if [ -n "$IMAGE_ID" ]; then
        EXCLUDE_IMAGE_IDS="$EXCLUDE_IMAGE_IDS $IMAGE_ID"
    fi
done

# Trim leading and trailing spaces
EXCLUDE_IMAGE_IDS=$(echo $EXCLUDE_IMAGE_IDS | xargs)

# Print the result
echo "Excluded Image IDs: $EXCLUDE_IMAGE_IDS"

# 특정 이미지를 제외한 모든 이미지 ID를 가져와 삭제합니다.
docker rm $(docker ps -aq)

# Convert the exclude image IDs to a grep pattern
EXCLUDE_PATTERN=$(echo $EXCLUDE_IMAGE_IDS | sed 's/ /\\|/g')

# Delete images that do not match the exclude pattern
docker images -q | grep -vE "$EXCLUDE_PATTERN" | xargs -r docker rmi
