## R Assessment

#### Q1. How does a matrix differ from a data frame?

- [x] A matrix may contain numeric values only.
- [ ] A matrix must not be singular.
- [ ] A data frame may contain variables that have different modes.
- [ ] A data frame may contain variables of different lengths.

#### Q2. What value does this statement return?

`unclass(as.Date("1971-01-01"))`

- [ ] 1
- [x] 365
- [ ] 4
- [ ] 12

#### Q3. What do you use to take an object such as a data frame out of the workspace?

- [x] remove()
- [ ] erase()
- [ ] detach()
- [ ] delete()

#### Q4. Review the following code. What is the result of line 3?

```r
xvect<-c(1,2,3)
xvect[2] <- "2"
xvect
```

- [ ] [1] 1 2 3
- [ ] [1] "1" 2 "3"
- [x] [1] "1" "2" "3"
- [ ] [1] 7 9

#### Q5. The variable height is a numeric vector in the code below. Which statement returns the value 35?

- [ ] `height(length(height))`
- [x] `height[length(height)]`
- [ ] `height[length[height]]`
- [ ] `height(5)`

#### Q6. In the image below, the data frame is named rates. The statement `sd(rates[, 2])` returns 39. As what does R regard Ellen's product ratings?

![Image](https://i.ibb.co/jvPPSRk/Captura-de-pantalla-2020-07-14-a-las-20-58-09.png)

- [ ] sample with replacement
- [ ] population
- [ ] trimmed sample
- [x] sample <-- not sure

#### Q7. Which choice does R regard as an acceptable name for a variable?

- [ ] Var_A!
- [ ] \_VarA
- [ ] .2Var_A
- [x] Var2_A

#### Q8. What is the principal difference between an array and a matrix?

- [x] A matrix has two dimensions, while an array can have three or more dimensions.
- [ ] An array is a subtype of the data frame, while a matrix is a separate type entirely.
- [ ] A matrix can have columns of different lengths, but an array's columns must all be the same length.
- [ ] A matrix may contain numeric values only, while an array can mix different types of values.

#### Q9. Which is not a property of lists and vectors?

- [ ] type
- [ ] length
- [ ] attributes
- [x] scalar

#### Q10. In the image below, the data frame on lines 1 through 4 is names StDf. State and Capital are both factors. Which statement returns the results shown on lines 6 and 7?

![Image](https://i.ibb.co/8DL1HCV/Captura-de-pantalla-2020-07-14-a-las-18-33-34.png)

- [ ] StDf[1:2,-3]
- [x] StDf[1:2,1]
- [ ] StDf[1:2,]
- [ ] StDf[1,2,]

#### Q11. Which function displays the first five rows of the data frame named pizza?

- [ ] BOF(pizza, 5)
- [ ] first(pizza, 5)
- [ ] top(pizza, 5)
- [x] head(pizza, 5)

#### Q12. You accidentally display a large data frame on the R console, losing all the statements you entered during the current session. What is the best way to get the prior 25 statements back?

- [ ] console(-25)
- [ ] console(reverse=TRUE)
- [ ] history()
- [x] history(max.show = 25)

#### Q13. d.pizza is a data frame. It's column named temperature contains only numbers. If u extract temperature using the [] accessors, its class defaults to numeric. How can you access temperature so that it retains the class of data.frame?

```
> class( d.pizza[ , "temperature" ] )
> "numeric"
```

- [ ] `class( d.pizza( , "temperature" ) )`
- [ ] `class( d.pizza[ , "temperature" ] )`
- [ ] `class( d.pizza$temperature )`
- [x] `class( d.pizza[ , "temperature", drop=F ] )`

#### Q14. What does c contain?

```
a <- c(3,3,6.5,8)
b <- c(7,2,5.5,10)
c <- a < b
```

- [ ] [1] NaN
- [ ] [1] -4
- [ ] [1] 4 -1 -1 2
- [x] [1] TRUE FALSE FALSE TRUE

#### Q15. Review the statements below. Does the use of the dim function change the class of y, and if so what is y's new class?

```
> y <- 1:9
> dim(y) <- c(3,3)
```

- [ ] No, y's new class is "array".
- [x] Yes, y's new class is "matrix".
- [ ] No, y's new class is "vector".
- [ ] Yes, y's new class is "integer".

#### Q16. What is `mydf$y` in this code?

`mydf <- data.frame(x=1:3, y=c("a","b","c"), stringAsFactors=FALSE)`

- [ ] list
- [ ] string
- [ ] factor
- [x] character vector

#### Q17. How does a vector differ from a list?

- [ ] Vectors are used only for numeric data, while list are useful for both numeric and string data.
- [ ] Vectors and lists are the same thing and can be used interchangeably.
- [x] A vector contains items of a single data type, while a list can contain items of different data types.
- [ ] Vectors are like arrays, while lists are like data frames.

#### Q18. What statement shows the objects on your workspace?

- [ ] list.objects()
- [ ] print.objects()
- [ ] getws()
- [x] ls()

#### Q19. What function joins two or more column vectors to form a data frame?

- [ ] rbind()
- [x] cbind()
- [ ] bind()
- [ ] coerce()

#### Q20. Review line 1 below. What does the statement in line 2 return?

```r
1 mylist <- list(1,2,"C",4,5)
2 unlist(mylist)
```

- [ ] [1] 1 2 4 5
- [ ] "C"
- [x] [1] "1" "2" "C" "4" "5"
- [ ] [1] 1 2 C 4 5

#### Q21. What is the value of y in this code?

```r
x <- NA
y <- x/1
```

- [ ] Inf
- [ ] Null
- [ ] NaN
- [x] NA

#### Q22. Two variable in the mydata data frame are named Var1 and Var2. How do you tell a bivariate function, such as cor.test, which two variables you want to analyze?

- [ ] `cor.test(Var1 ~ Var2)`
- [ ] `cor.test(mydata$(Var1,Var2))`
- [x] `cor.test(mydata$Var1,mydata$Var2)`
- [ ] `cor.test(Var1,Var2, mydata)`

#### Q23. A data frame named d.pizza is part of the DescTools package. A statement is missing from the following R code and an error is therefore likely to occur. Which statement is missing?

```r
library(DescTools)
deliver <- aggregate(count,by=list(area,driver), FUN=mean)
print(deliver)
```

- [x] `attach(d.pizza)`
- [ ] `summarize(deliver)`
- [ ] `mean <- rbind(d.pizza,count)`
- [ ] `deliver[!complete.cases(deliver),]`

#### Q24. How to name rows and columns in DataFrames and Matrices F in R?

- [ ] data frame: names() and rownames() matrix: colnames() and row.names()
- [x] data frame: names() and row.names() matrix: dimnames() (not sure)
- [ ] data frame: colnames() and row.names() matrix: names() and rownames()
- [ ] data frame: colnames() and rownames() matrix: names() and row.names()

#### Q25. Which set of two statements-followed by the cbind() function-results in a data frame named vbound?

- [ ]

```r
v1<-list(1,2,3)
v2<-list(c(4,5,6))
vbound<-cbind(v1,v2)
```

- [ ]

```r
v1<-c(1,2,3)
v2<-list(4,5,6))
vbound<-cbind(v1,v2)
```

- [ ]

```r
v1<-c(1,2,3)
v2<-c(4,5,6))
vbound<-cbind(v1,v2)
```

- [ ]

#### Q26. ournames is a character vector. What values does the statement below return to Cpeople?

`Cpeople <- ournames %in% grep("^C", ournames, value=TRUE)`

- [ ] records where the first character is a C
- [ ] any record with a value containing a C
- [ ] TRUE or FALSE, depending on whether any character in ournames is C
- [x] TRUE or FALSE values, depending on whether the first character in an ournames record is C

#### Q27. What is the value of names(v[4])?

```r
v <- 1:3
names(v) <- c("a", "b", "c")
v[4] <- 4
```

- [x] ""
- [ ] d
- [ ] NULL
- [ ] NA

#### Q28. Which of the following statements doesn't yield the code output below:

Review the following code. What is the result of line 3?

```r
x <- c(1, 2, 3, 4)

Output: [1] 2 3 4
```

- [ ] x[c(2, 3, 4)]
- [ ] x[-1]
- [ ] x[c(-1, 0, 0, 0)]
- [x] x[c(-1, 2, 3, 4)]

#### Q29. Given DFMerged <- merge(DF1, DF2) and the image below, how manu rows are in DFMerged?

```
DF1(data frame 1): DF2(data frame 2):
VarA VarB VarA VarD
1 1 2 1 18 21
2 4 5 2 19 22
3 7 8 3 20 23
```

- [ ] 6
- [ ] 9
- [ ] 3
- [x] 0
