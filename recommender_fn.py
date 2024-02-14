import pickle

with open('final_cluster.pkl', 'rb') as file:
    final_cluster = pickle.load(file)

def distillery_rec():
    distillery_list = " ".join([distillery for distillery in final_cluster['Distillery']])
    print("Available Distilleries:",distillery_list)

    choice = input("Which Distillery do you want something similar to? (Enter 'Idk what I want' if unsure): ").lower()
    
    if choice == 'idk what i want':
        print('The Top 3 rated Distilleries are', 'Lagavulin', 'Ardbeg', 'Laphroaig')
        print('The Author\'s favourite Distillery is Balvenie')
        print('Once you\'ve chosen your distillery, just pick a bottle in your price range.')
        print('The older the better, but if you\'re not sure, just go with the 12 year old.')
        print('If you pick a very cheap bottle, you\'ll probably get a blend, which is fine, but they are better mixed with coke.')
        print('If you get a Single Malt, you can drink it neat, or with a little water to open up the flavours.')
        return 
    else:
        # Find the cluster of the given distillery name
        cluster = final_cluster[final_cluster['Distillery'].str.lower() == choice]['Cluster'].values[0]
        
        # Find all distilleries with the same cluster
        distilleries_same_cluster = final_cluster[final_cluster['Cluster'] == cluster]['Distillery']
        
        # Print distilleries with the same cluster
        print(f"Distilleries in the same cluster as {choice}:")
        for distillery in distilleries_same_cluster:
            print(distillery)
        return 'all done!'

# run function
distillery_rec()
