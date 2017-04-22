# switch-users-to-staff
Changes the record_type for all Alma users listed in a CSV file of user IDs to type 'STAFF'. 

#### Create a file of user IDs to update (user_ids.csv)
In Alma Analytics:
- Navigate to the Users subject area.  
- Select the Primary Identifier column (this is what will be used to look up all of the exported users)
- Add any filters needed to narrow down the list of users to those you wish to update.  In this case, you can add the Role Type element and select all roles that are not 'Patron'.  
- After applying the role type filter, delete the Role Type column from the Selected Columns area.  We want to end up with a report that only contains user IDs.  
- Click on Results to run this analysis.  
- Once you are happy with your analysis results, export the list of user IDs by going to Export this Analysis | Data | CSV Format.  
You are now ready to run the following script

#### config.txt
```
[Params]
apikey: [apikey] 
baseurl: https://api-na.hosted.exlibrisgroup.com
```

#### switch_to_staff.py
Run as 
`python ./switch_to_staff.py config.txt user_ids.csv`
