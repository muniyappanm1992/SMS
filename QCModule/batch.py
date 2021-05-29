import pandas as pd
df_yvrokar=pd.read_excel(r'D:\Python\Projects\Django\Terminal Stuff\DryOut\yvrokar.XLSX')
df_yqlab=pd.read_excel(r'D:\Python\Projects\Django\Terminal Stuff\DryOut\yqlab.XLSX')
df_batch=pd.read_excel(r'D:\Python\Projects\Django\Terminal Stuff\DryOut\batch.XLSX')
boolean = df_yvrokar['Tank'].isna()
df_yvrokar = df_yvrokar[~boolean]
df_yvrokar["QtyDiff"] = df_yvrokar["Physical Balance"] - df_yvrokar["Quantity"]
df_yvrokar["QtyDiff"] = df_yvrokar["QtyDiff"].map(lambda x: round(x, 2))
df_yvrokar["Status"] = df_yvrokar["QtyDiff"].map(lambda x: "Dormant" if abs(x) < 10 else ("Receipt" if x > 10 else "Dispatch"))
df_yvrokar["Suggest_Batch"]=""
# for i,data in enumerate(df_yvrokar):
indexNo=[]
batch_suggest=[]
df_yvrokar.reset_index( inplace=True)
print(df_yvrokar["Status"].values.tolist())
for i,data in enumerate(df_yvrokar["Status"].values.tolist()):
    print(i)
    if(data=="Receipt"):
        tank=df_yvrokar['Tank'].values.tolist()[i]
        df=df_batch[df_batch['Storage Tank']==tank]
        print(df)
        if(len(df)>0):
            batchNo=[]
            part_batch=""
            for j,batch in enumerate(df["Batch"].values.tolist()):
                batch_split_list=batch.split("/")
                for z,part in enumerate(batch_split_list):
                    if(z==0):
                        part_batch=part
                    elif(z<len(batch_split_list)-1):
                        part_batch=part_batch+"/"+part
                if(tank==batch_split_list[-2]):
                    batchNo.append(int(batch_split_list[-1]))
            new_batchNo=max(batchNo)+1
            new_batch=part_batch+"/"+str(new_batchNo)
            print(i)
            df_yvrokar.at[i, 'Suggest_Batch'] = new_batch
            print(new_batch)
    elif(data=="Dispatch"):
        pass
print(df_yvrokar)
boolean = df_yqlab['Inspection Lot'].isna()
df_yqlab = df_yqlab[~boolean]
df_yqlab=df_yqlab[df_yqlab['Sample Type']=="COMPOSITE"]
df_new=pd.merge(left=df_yvrokar,right=df_yqlab,how='inner',left_on=['Suggest_Batch'],right_on=['Batch'])
print(df_new)


