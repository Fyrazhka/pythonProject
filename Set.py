def main():
    list=['rap','house','electronic music', 'rap']
    setlist=set(list)
    print(setlist)
    print(sum([1,2,2,1])==sum(set([1,2,2,1])))

    album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
    album_set2 = set(["AC/DC", "Back in Black", "The Dark Side of the Moon"])
    album_set3=album_set1.union(album_set2)  #set1 + set2
    print(album_set3)
    print (album_set1.issubset(album_set3))   #one in second
    album_set4=album_set1 & album_set2 # general in set1 and set2
    print(album_set4)
if __name__ == '__main__':
    main()