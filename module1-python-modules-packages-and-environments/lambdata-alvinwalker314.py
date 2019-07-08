def split_date(df, date_column):
	years= [data.split('/')[0] for data in df[date_column]]
	months= [data.split('/')[1] for data in df[date_column]]
	days= [data.split('/')[2] for data in df[date_column]]
	df['year']= years
	df['month']= months
	df['day']= days
	return df

def list_series_dataframe(data, column_name):
  series= pd.Series(data) #turn list into a pandas series
  df= pd.DataFrame(columns=column_name, data=data) #turn list into a pandas dataframe
  return df #returning new dataframe
