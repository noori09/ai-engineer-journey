# my favourite movies
movies = ["Veer-Zara","Singh is King","Ajab Prem Ki Gajab Kahani","3 Idiots"]

print("All movies",movies)
print("First movie",movies[0])
print("Last movie",movies[-1])
print("Second last movie",movies[-2])
print("Total movies",len(movies))

#Add a new fav movie
movies.append("Hera Pheri")
print("After adding",movies)

#Insert at position 1
movies.insert(1,"Dangal")
print("After insertion",movies)

#Remove one
movies.remove("Hera Pheri")
print("After removing",movies)

#Check if movie is in the list
print("Is Dangal there?","Dangal" in movies)
print("Is Hera Pheri there?", "Hera Pheri" in movies)