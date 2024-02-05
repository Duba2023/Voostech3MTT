#Raw data from wikipeida
url_link = 'https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue'

#Reading a html file
lst_company = pd.read_html(url_link)

lst_company = lst_company[0] #Dataframe

#Displaying the first three rows
lst_company.head(3)

#Taking away the second heading , leaving the first one
lst_company.columns = lst_company.columns.get_level_values(0)

#Renaming the columns
lst_company.rename(columns={"Headquarters[note 1]": "Headquarters"} , inplace=True)

#Removing a $ sign from Revenue and Profit values
lst_company['Revenue'] = lst_company['Revenue'].str.replace('$', '')

lst_company['Profit'] = lst_company['Profit'].str.replace('$', '')

#Deleting a column
lst_company.drop( columns = ['Ref.'], axis = 1, inplace = True) 

lst_company.drop( columns = ['Unnamed: 9_level_0'], axis = 1, inplace = True)
lst_company['Industry'].value_counts()

#Grouping the industries and ploting a barchat to know the highest 
lst_company.groupby('Industry').count().plot(kind = 'bar')

#Renaming columns
lst_company.rename( columns = {'Revenue' : 'Revenue($)'} , inplace = True)
lst_company.rename( columns = {'Profit' : 'Profit($)'} , inplace = True)

# Removing a sign and replacing with nothing
lst_company['Profit($)'] = lst_company['Profit($)'].str.replace('−' , '')

#Renaming columns
lst_company.rename( columns = {'Rank' : 'Ranking' , 'Name': ' Company Name'} , inplace = True)

#copying lst_company and puting it in lst_company1
lst_company1 = lst_company.copy()

# Displaying the list of industry and their corresponding numbers of missing values
lst_company1.isnull

#Dropping an industry with the highest missing values 
lst_company1 = lst_company1.drop(index=49)

