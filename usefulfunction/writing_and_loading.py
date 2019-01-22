import pickle
my_favorite_thing = [
    'laptop','Bag','Tv','Ipad','Book','Mobile phone'
]

writing_to_file = open('favorites.dat','wb')
pickle.dump(my_favorite_thing,writing_to_file)
writing_to_file.close()