# Fitbit Dataset

This folder should contain your Fitbit CSV export files.

## Expected Files

- `dailyActivity_merged.csv` - Daily activity metrics (steps, calories, distance, etc.)
- `sleepDay_merged.csv` - Sleep tracking data

## Getting Your Data

1. Go to [fitbit.com](https://www.fitbit.com)
2. Log in to your account
3. Navigate to Settings → Data Export
4. Request your data archive
5. Download and extract the CSV files
6. Place them in this folder

## Sample Data Structure

### dailyActivity_merged.csv
```
Id,ActivityDate,TotalSteps,TotalDistance,Calories,VeryActiveMinutes,FairlyActiveMinutes,LightlyActiveMinutes,SedentaryMinutes
1234567890,4/12/2016,13162,8.5,1985,25,13,328,728
```

### sleepDay_merged.csv
```
Id,SleepDay,TotalSleepRecords,TotalMinutesAsleep,TotalTimeInBed
1234567890,4/12/2016 12:00:00 AM,1,327,346
```

## Privacy Note

This folder is included in `.gitignore` to protect your personal data. Your Fitbit data will not be committed to version control.
