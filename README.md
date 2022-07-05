# Tools-For-Data-Analysis

capitals = pd.DataFrame([["Alabama","AL"],
["Alaska","AK"],["Arizona","AZ"],["Arkansas","AR"],["California","CA"],["Colorado","CO"],["Connecticut","CT"],
["Delaware","DE"],["Florida","FL"],["Georgia","GA"],["Hawaii","HI"],["Idaho","ID"],["Illinois","IL"],
["Indiana","IN"],["Iowa","IA"],["Kansas","KS"],["Kentucky""KY"],["Louisiana","LA"],
 ["Maine","ME"],["Maryland","MD"],["Massachusetts","MA"],["Michigan","MI"],["Minnesota","MN"],["Mississippi","MS"],
["Missouri","MO"],["Montana","MT"],["Nebraska","NE"],["Nevada","NV"],["New Hampshire","NH"],["New Jersey","NJ"],
["New Mexico","NM"],["New York","NY"],["North Carolina","NC"],["North Dakota","ND"],["Ohio","OH"],["Oklahoma","OK"],
["Oregon","OR"],["Pennsylvania","PA"],["Rhode Island","RI"],["South Carolina","SC"],["South Dakota","SD"],["Tennessee","TN"],
["Texas","TX"],["Utah","UT"],["Vermont","VT"],["Virginia","VA"],["Washington","WA"],["West Virginia","WV"],["Wisconsin","WI"],
["Wyoming","WY"]], columns = ['state', 'abbrev'])
na_dam_data=capitals.set_index('abbrev')  # setting columns_ID as index.
dict_value=dict(na_dam_data)
dict_value
df['state']=[dict_value['state'][i] if i in dict_value['state'] else None  for i in df['GESTFIPS_data']]
