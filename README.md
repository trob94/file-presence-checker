# File Checker Project

Automatically checks if README.md and .gitignore exist in the repository and logs results to AWS CloudWatch.

## How to Set Up GitHub Secrets

1. Go to repository **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret** and add these 3 secrets:
   - `AWS_ACCESS_KEY_ID` - Your AWS access key
   - `AWS_SECRET_ACCESS_KEY` - Your AWS secret key  
   - `AWS_REGION` - Your AWS region (like us-east-1)

Get these values from AWS IAM when you create a user with CloudWatch permissions.

Also covered in my writeup on Medium

## How to Run File Check Manually

```bash
python verify_required_files.py
```

**Success**: Shows "All required files are present"  
**Failure**: Shows "ERROR: [filename] is missing!" and exits

## How AWS CLI Logging Works

The workflow does two things:

1. **Creates log stream**: Makes a dated container for log messages
2. **Sends log event**: Writes a message with who triggered the workflow and when

```yaml
aws logs create-log-stream --log-group-name "LOG_GROUP" --log-stream-name "2025-08-22"
aws logs put-log-events --log-group-name "LOG_GROUP" --log-events message="Check passed by username"
```

## Where to Find CloudWatch Logs

1. Go to **AWS CloudWatch Console**
2. Click **Log groups**
3. Choose your environment:
   - **Beta logs** (PRs): `/github-actions/required-files-checker/beta`
   - **Prod logs** (main branch): `/github-actions/required-files-checker/prod`
4. Click on any log stream (dated) to see messages

## What Happens When Files Are Missing

1. **Python script fails** with error message
2. **GitHub Actions shows red X** in Actions tab
3. **Pull requests get blocked** until files are added
4. **No CloudWatch log** is sent (only successful runs log)

**Fix**: Add the missing files and commit them. The workflow runs again automatically.
