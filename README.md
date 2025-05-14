Try AI directly in your favorite apps … Use Gemini to generate drafts and refine content, plus get Gemini Advanced with access to Google’s next-gen AI for $19.99 $0 for 1 month
README.md
# SQL DB Backup Archive Lambda

This folder contains an AWS Lambda function written in Python that automates the archival of SQL database backup files uploaded to an S3 bucket.

## What the Script Does
- **Trigger:** The Lambda is triggered by S3 events when a new file is uploaded to a specified S3 bucket.
- **File Filtering:** It checks if the uploaded file's key (name) ends with `.zip` and if the last 10 characters of the key start with `01` (indicating a specific date or naming convention).
- **Archival:** If the conditions are met, the script copies the `.zip` file from the source S3 bucket to a target S3 bucket defined by the `TARGET_S3_BUCKET` environment variable.
- **Logging:** The script logs details about the event, the source and target buckets, and Lambda context information for debugging and traceability.
- **Error Handling:** If any error occurs during the copy process, it is logged and returned by the function.

## Usage
- Deploy this Lambda function in AWS.
- Set up an S3 event trigger for object creation events on the source bucket.
- Set the `TARGET_S3_BUCKET` environment variable in the Lambda configuration to specify the destination bucket for archival.

## Requirements
- AWS Lambda execution role with permissions to read from the source S3 bucket and write to the target S3 bucket.
- Python 3.x runtime.
- The `boto3` library (available in the AWS Lambda Python runtime by default).

## File
- `sql-db-backup-archive.py`: The main Lambda handler script.
