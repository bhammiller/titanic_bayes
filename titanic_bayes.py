
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
Location="titanic3.xls"
df = pd.read_excel(Location)
df.head()


# In[4]:


df.head()


# In[7]:


total_survivors=df['survived'].sum()
total_fclass_survivors=df['first_class_survivor'].sum()
total_sclass_survivors=df['second_class_survivor'].sum()
total_tclass_survivors=df['third_class_survivor'].sum()
total_boy_survivors=df['boy_survivor'].sum()
total_woman_survivors=df['woman_survivor'].sum()
total_man_survivors=df['man_survivor'].sum()
total_boys=df['boy'].sum()
total_women=df['woman'].sum()
total_men=df['man'].sum()
total_first_class=323
total_second_class=277
total_third_class=709
print(total_survivors)
print(total_fclass_survivors)
print(total_sclass_survivors)
print(total_tclass_survivors)
print(total_boy_survivors)
print(total_woman_survivors)
print(total_man_survivors)
print(total_boys)
print(total_women)
print(total_men)


# In[2]:


pd.value_counts(df['pclass'])


# In[6]:


df['first_class_survivor']=np.where((df['pclass']==1)&(df['survived']==1),1,0)
df['second_class_survivor']=np.where((df['pclass']==2)&(df['survived']==1),1,0)
df['third_class_survivor']=np.where((df['pclass']==3)&(df['survived']==1),1,0)

df['boy']=np.where((df['age']<=17)&(df['sex']=='male'),1,0)
df['woman']=np.where((df['age']>=17)&(df['sex']=='female'),1,0)
df['man']=np.where((df['age']>=17)&(df['sex']=='male'),1,0)

df['boy_survivor']=np.where((df['age']<=17)&(df['sex']=='male')&(df['survived']==1),1,0)
df['woman_survivor']=np.where((df['age']>=17)&(df['sex']=='female')&(df['survived']==1),1,0)
df['man_survivor']=np.where((df['age']>=17)&(df['sex']=='male')&(df['survived']==1),1,0)


# In[10]:


prob_Survivor=total_survivors/1308
prob_Survivor_First_Class=total_fclass_survivors/total_survivors
prob_Survivor_Second_Class=total_sclass_survivors/total_survivors
prob_Survivor_Third_Class=total_tclass_survivors/total_survivors
#age of adult is 17
prob_Survivor_Boy=total_boy_survivors/total_survivors
prob_Survivor_Woman=total_woman_survivors/total_survivors
prob_Survivor_Man=total_man_survivors/total_survivors
def computeBayes(pass_class, sex_age, survival):
    return pass_class * sex_age * survival
prob_second_boy=round(computeBayes(prob_Survivor_Second_Class,prob_Survivor_Boy,prob_Survivor),4)
prob_third_woman=round(computeBayes(prob_Survivor_Third_Class,prob_Survivor_Woman,prob_Survivor),4)
prob_first_man=round(computeBayes(prob_Survivor_First_Class,prob_Survivor_Man,prob_Survivor),4)
print('The probability that a survivor is a second class boy is ' + str(prob_second_boy))
print('The probability that a survivor is a third class woman is ' + str(prob_third_woman))
print('The probability that a survivor is a first class man is ' + str(prob_first_man))


# In[9]:


#second attempt
prob_Survivor=total_survivors/1308
prob_First_Class_Survive=total_fclass_survivors/total_first_class
prob_Second_Class_Survive=total_sclass_survivors/total_second_class
prob_Third_Clas_Survive=total_tclass_survivors/total_third_class
'''
prob_Boy_First_Class=total_fclass_survivors/total_first_class
prob_Boy_Second_Class=total_sclass_survivors/total_second_class
prob_Boy_Third_Clas=total_tclass_survivors/total_third_class
'''
prob_Boy_Survive=total_boy_survivors/total_boys
prob_Woman_Survive=total_woman_survivors/total_women
prob_Man_Survive=total_man_survivors/total_men

prob_Boy = total_boys/1308
prob_Woman = total_women/1308
prob_Man = total_men/1308

print(prob_First_Class_Survive)
print(prob_Second_Class_Survive)
print(prob_Third_Clas_Survive)
print(prob_Boy_Survive)
print(prob_Woman_Survive)
print(prob_Man_Survive)


# In[ ]:


"""
def computeBayes_v2(pass_class, sex_age, survival):
    return pass_class * sex_age * survival
prob_second_boy_v2=round(computeBayes_v2(prob_Second_Class_Survive,prob_Survivor_Boy,prob_Survivor),4)
prob_third_woman_v2=round(computeBayes_v2(prob_Survivor_Third_Class,prob_Survivor_Woman,prob_Survivor),4)
prob_first_man_v2=round(computeBayes_v2(prob_Survivor_First_Class,prob_Survivor_Man,prob_Survivor),4)
print('The probability that a survivor is a second class boy is ' + str(prob_second_boy))
print('The probability that a survivor is a third class woman is ' + str(prob_third_woman))
print('The probability that a survivor is a first class man is ' + str(prob_first_man))
"""

