#! /bin/bash

PROJECT_ROOT="$(cd "$(dirname $0)" && cd .. && pwd)"
DATA_DIRECTORY="$PROJECT_ROOT/data"
REVIEW_DATA_DEV_FILE="$DATA_DIRECTORY/review-data-dev.json"
BUSINESS_DATA_DEV_FILE="$DATA_DIRECTORY/business-data-dev.json"
BUSINESS_ID_FILE="$DATA_DIRECTORY/business_ids.txt"
TEMP_DIRECTORY="$PROJECT_ROOT/tmp"

REVIEW_DATA_FULL_FILE_PATH="$1"
BUSINESS_DATA_FULL_FILE_PATH="$2"

error_message() {
  echo "$(tput setaf 1)$1$(tput sgr0)"
}

success_message() {
  echo "$(tput setaf 2)$1$(tput sgr0)"
}

# Initialize temp directory
if [ -d $TEMP_DIRECTORY ]; then
  rm -rf $TEMP_DIRECTORY
fi
mkdir -p $TEMP_DIRECTORY

# Check for jq executable
if ! command -v jq > /dev/null 2> /dev/null; then
  error_message "JQ is required to parse JSON data; download it at:"
  error_message "https://stedolan.github.io/jq/"
  exit 1
fi

# Make sure that the required variables are set
if [[ -z $REVIEW_DATA_FULL_FILE_PATH ]]; then
  error_message "First argument should be the path to the full review data file"
  exit 1
fi

if [[ -z $BUSINESS_DATA_FULL_FILE_PATH ]]; then
  error_message "Second argument should be the path to the full business data file"
  exit 1
fi

# Start in project root
cd $PROJECT_ROOT

if [ ! -d "$DATA_DIRECTORY" ]; then
  error_message "Creating data directory"
  mkdir ./data
else
  success_message "Found existing data directory"
fi

# Create review data file
if [ ! -f $REVIEW_DATA_DEV_FILE ]; then
  error_message "Creating development review data"
  head -1000 ./yelp_academic_dataset_review.json > $REVIEW_DATA_DEV_FILE
else
  success_message "Found development review data"
fi

# Create business ID file
if [ ! -f $BUSINESS_ID_FILE ]; then
  error_message "Creating business ID file"
  TEMP_BUSINESS_ID_FILE="$TEMP_DIRECTORY/business_ids.txt"

  business_ids=()
  while read -r line; do
    echo $line | jq '.business_id' >> $TEMP_BUSINESS_ID_FILE
  done < "$REVIEW_DATA_DEV_FILE"

  sort -n $TEMP_BUSINESS_ID_FILE | uniq > $BUSINESS_ID_FILE
else
  success_message "Found business ID file"
fi

# Build the business data from the review data
if [ ! -f $BUSINESS_DATA_DEV_FILE ]; then
  error_message "Creating business dev file; this might take a while..."

  while read -r line; do
    echo $line | fgrep -f $BUSINESS_ID_FILE >> $BUSINESS_DATA_DEV_FILE
  done < "$BUSINESS_DATA_FULL_FILE_PATH"
else
  success_message "Found business dev file"
fi

# Clean up temp directory
if [ -d $TEMP_DIRECTORY ]; then
  success_message "Cleaning up..."
  rm -rf $TEMP_DIRECTORY
fi
