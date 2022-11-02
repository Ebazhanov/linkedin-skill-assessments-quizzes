## R (Programming Language)

#### Q1. How does a matrix differ from a data frame?

- [ ] A matrix may contain numeric values only.
- [ ] A matrix must not be singular.
- [x] A data frame may contain variables that have different modes.
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

```
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

![Image](https://i.ibb.co/jvPPSRk/Captura-de-pantalla-2020-07-14-a-las-20-58-09.png?raw=png)

- [ ] sample with replacement
- [ ] population
- [ ] trimmed sample
- [x] sample <-- not sure

#### Q7. Which choice does R regard as an acceptable name for a variable?

- [ ] `Var_A!`
- [ ] `\_VarA`
- [ ] `.2Var_A`
- [x] `Var2_A`

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

#### Q10. In the image below, the data frame on lines 1 through 4 is named StDf. State and Capital are both factors. Which statement returns the results shown on lines 6 and 7?

![Image](https://i.ibb.co/8DL1HCV/Captura-de-pantalla-2020-07-14-a-las-18-33-34.png?raw=png)

- [ ] StDf[1:2,-3]
- [x] StDf[1:2,1]
- [ ] StDf[1:2,]
- [ ] StDf[1,2,]

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

#### Q13. d.pizza is a data frame. It's a column named temperature contains only numbers. If you extract temperature using the [] accessors, its class defaults to numeric. How can you access temperature so that it retains the class of data.frame?

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

- [ ] Vectors are used only for numeric data, while lists are useful for both numeric and string data.
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

```
1 mylist <- list(1,2,"C",4,5)
2 unlist(mylist)
```

- [ ] [1] 1 2 4 5
- [ ] "C"
- [x] [1] "1" "2" "C" "4" "5"
- [ ] [1] 1 2 C 4 5

#### Q21. What is the value of y in this code?

```
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

```
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

#### Q26. ournames is a character vector. What values does the statement below return to Cpeople?

`Cpeople <- ournames %in% grep("^C", ournames, value=TRUE)`

- [ ] records where the first character is a C
- [ ] any record with a value containing a C
- [ ] TRUE or FALSE, depending on whether any character in ournames is C
- [x] TRUE and FALSE values, depending on whether the first character in an ournames record is C

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

#### Q28. Which of the following statements doesn't yield the code output below. Review the following code. What is the result of line 3?

```r
x <- c(1, 2, 3, 4)
Output: [1] 2 3 4
```

- [ ] x[c(2, 3, 4)]
- [ ] x[-1]
- [ ] x[c(-1, 0, 0, 0)]
- [x] x[c(-1, 2, 3, 4)]

#### Q29. Given DFMerged <- merge(DF1, DF2) and the image below, how manu rows are in DFMerged?

![image](https://user-images.githubusercontent.com/52632898/139964478-9806a163-76b2-4f99-97bc-c925fdf6e388.png?raw=png)

- [ ] 6
- [ ] 9
- [ ] 3
- [x] 0

#### Q30. What does R return in response to the final statement?

```r
x<-5:8
names(x)<-letters[5:8]
x
```

- [ ] e f g h
      "5" "6" "7" "8"
- [ ] 5 6 7 8
- [ ] e f g h
- [x] e f g h
      5 6 7 8

#### Q31. How do you return "October" from x in this code?

```r
x<-as.Date("2018-10-01")
```

- [ ] attr()
- [x] months(x)
- [ ] as.month(x)
- [ ] month(x)

#### Q32. How will R respond to the last line of this code?

```r
fact<-factor(c("Rep","Dem","Dem","Rep"))
fact
[1] Rep Dem Dem Rep
Levels: Rep Dem
fact[2]<-"Ind"
```

- [ ] >
- [ ] [,2]Ind
- [x] invalid factor level, NA generated
- [ ] Ind

#### Q33. What does R return?

```r
StartDate<- as.Date("2020/2/28")
StopDate<- as.Date("2020/3/1")
StopDate-StartDate
```

- [ ] "1970-01-02"
- [ ] time difference of one day
- [x] time difference of two days
- [ ] error in x-y: nonnumeric argument to binary operator

#### Q34. What does the expression `mtrx * mtrx` do ?

```r
> mtrx <- matrix( c(3,5,8,4), nrow= 2,ncol=2,byrow=TRUE)
> newmat <- mtrx * mtrx
```

- [ ] it transpose **mtrx**
- [ ] it premultiplies the current **netwmat** row by the **newmat** column.
- [ ] it returns the results of a matrix multiplication
- [x] It squares each cell in **mtrx**

```r
> newmat
     [,1] [,2]
[1,]    9   25
[2,]   64   16

# The `%*%` operator gives matrix multiplication
> mtrx %*% mtrx
     [,1] [,2]
[1,]   49   35
[2,]   56   56
```

#### Q35. Which function in R combines different values into a single object?

- [ ] connect()
- [ ] concat()
- [ ] contact()
- [x] c()

#### Q36. Which file contains settings that R uses for all users of a given installation of R?

- [ ] Rdefaults.site
- [ ] Renviron.site
- [x] Rprofile.site
- [ ] Rstatus.site

#### Q37. If **mdf** is a data frame, which statement is true ?

- [x] **ncol(mdf)** equals **length(mdf)**.
- [ ] The number of rows must equals the number of columns.
- [ ] The legnth of any column in **mdf** may differ from any other column in **mdf**
- [ ] All columns must have the same data type.

#### Q38. A list can contain a list as an element. **MyList** has five columns, and the third column's item is a list of three items. How do you put all seven values in **MyList** into a single vector?

- [ ] vector(MyList, length = 7)
- [ ] coerce(MyList, nrows = 1)
- [x] unlist(MyList)
- [ ] coerce(MyList, nrows = 7)

#### Q39. Which strings could be returned by the function ls(path = "^V")?

- [ ] ANOVAData, anovadata
- [x] VisitPCA, VarX
- [ ] VisitPCA, varx
- [ ] Xvar, Yvar

#### Q40. StDf is a data frame. Based on this knowledge, what does this statement return?

```r
StDf[, -1]
```

- [ ] all but the first row and first column of StDf
- [ ] all but the final column of StDf
- [x] all but the first column of StDf
- [ ] only the first column of StDf

#### Q41. Which statement enables you to interactively open a single file?

- [ ] file.list()
- [ ] file.select()
- [x] file.choose()
- [ ] file.open()

#### Q42. How are these data types alike: logical, integer, numeric, and character?

- [ ] Each is a type of data frame.
- [x] Each is a type of atomic vector.
- [ ] Each is a type of complex vector.
- [ ] Each is a type of raw vector.

#### Q43. What does the `MyMat[ ,3]` subsetting operation return for this code?

```r
MyMat = matrix(c(7, 9, 8, 6, 10, 12),nrow=2,ncol=3, byrow = TRUE)
```

- [ ] :

```
[ ,3]
[1, ] 8
[2, ] 12
```

- [x] :

```
[1] 8 12
```

- [ ] :

```
[1] 10 12
```

- [ ] :

```
[ ,3]
[1, ] 10
[2, ] 12
```

#### Q44. What does the function `power.anova.test` return?

- [ ] the probability of making a Type I error
- [x] the probability of not making a Type II error
- [ ] the probability of making a Type II error
- [ ] the probability of not making a Type I error

#### Q45. Review the statement below. What is the effect of `covariate:factor` on the analysis?

```r
result <- lm(outcome ~ covariate + factor + covariate:factor, data = testcoef)
```

- [ ] It forces the intercepts of the individual regressions to zero.
- [x] It calls for the effect of the covariate **within each level of the factor**.
- [ ] It calls for the effect of each variable from covariate to factor in testcoef.
- [ ] It forces the covariate to enter the equation before the factor levels.

```r
# Example call to demonstrate.  `Species` is a Factor.  Petal.Length, Petal.Width are numeric.
# see `help(formula)` for more details on the formula specification.  `:` is "effect modification" or "interaction"

> summary(lm(Petal.Length ~ Petal.Width + Species + Petal.Width:Species, data = iris))
...
Petal.Width:Speciesversicolor   1.3228     0.5552   2.382   0.0185 *
Petal.Width:Speciesvirginica    0.1008     0.5248   0.192   0.8480
...
```

#### Q46. A variable whose type is numeric can contain which items?

- [ ] integers and real values
- [ ] integers, real, and raw values
- [x] real values only
- [ ] integers, real, and logical values

#### Q47. What is the legitimate name of a data class in R?

- [ ] property
- [x] integer
- [ ] number
- [ ] variant

#### Q48. How do you extract the values above the main diagonal from a square matrix named `Rmat`?

- [x] `Rmat[upper.tri(Rmat)]`
- [ ] `upper.triangular(Rmat)`
- [ ] `upper.tri(Rmat)`
- [ ] `upper.diag(Rmat)`

#### Q49. `x` is a vector of type integer, as shown on line 1 below. What is the type of the result returned by the statement > median(x)?

`x <- c(12L, 6L, 10L, 8L, 15L, 14L, 19L, 18L, 23L, 59L)`

- [ ] numeric
- [ ] integer
- [ ] single
- [x] double

#### Q50. A list named `a` is created using the statement below. Which choice returns TRUE?

`a <- list("10", TRUE, 5.6)`

- [x] is.list(a[1])
- [ ] is.numeric(a[1])
- [ ] is.logical(a[1])
- [ ] is.character(a[1])

#### Q51. How do you obtain the row numbers in a data frame named `pizza` for which the value of `pizza$delivery_min` is greater than or equal to 30?

- [ ] :

```r
late_delivery <- pizza$delivery_min >= 30
index_late <- index(late_delivery)
index_late
```

- [ ] :

```r
late_delivery <- pizza$delivery_min >= 30
rownum_late <- rownum(late_delivery)
rownum_late
```

- [x] :

```r
late_delivery <- pizza$delivery_min >= 30
which_late <- which(late_delivery)
which_late
```

- [ ] :

```r
late_delivery <- pizza$delivery_min >= 30
late <- piza$late_delivery
pizza$late
```

#### Q52. Which function returns `[1] TRUE FALSE TRUE`?

`indat <- c("Ash Rd","Ash Cir","Ash St")`

- [ ] grepl("[Rd|Ave|Dr|St]", indat)
- [x] grepl("Rd|Ave|Dr|St", indat)
- [ ] grepl("Rd,Ave,Dr,St", indat)
- [ ] grepl("[Rd],[Ave],[Dr],[St]", indat)

#### Q53. Which statement returns the fourth row of a data frame named _fish_?

- [x] fish[4, ]
- [ ] fish( ,4)
- [ ] fish(4, )
- [ ] fish{4, }

#### Q54. What is the value of _csum_?

```
a <- c(1.2, 2, 3.5, 4)
b <- c(1.2, 2.2, 3.5, 4)
csum <-sum(a == b)
```

- [ ] 8
- [x] 3
- [ ] 0.2
- [ ] 21.6

#### Q54. A list named _a_ is created using the statement below. Which choice returns TRUE?

```
a <- list("10", TRUE, 5.6)
```

- [x] is.list(a[1])
- [ ] is.numeric(a[1])
- [ ] is.logical(a[1])
- [ ] is.character(a[1])

#### Q55. What is the result of these three lines of code?

```r
vect1 <- c(1:4)
vect2 <- c(1:2)
vect1 * vect2
```

- [x] [1] 1 4 3 8 
- [ ] ERROR
- [ ] [1] 1 2 3 4 1 2
- [ ] [1] 1 2 3 4 2 4 6 8

#### Q56. Which choice returns [1] "2019-09-28"?

- [ ] format(as.POSIXct("Sep-28-2019 07:54:31 AM",format='%b%d%Y'))
- [ ] as.POSIXlt("Sep-28-2019 07:54:31 AM",format='%b-%d-%Y')
- [ ] as.POSIXct("Sep-28-2019 07:54:31 AM UTC")
- [x] format(as.POSIXct("Sep-28-2019 07:54:31 AM UTC",format='%b-%d-%Y'))

#### Q57. The variable potus is a character vector, as shown in line 1 below. Wich statement returns the results shown?

```r
1 potus <- c("GHW Bush", "Clinton", "GW Bush", "Obama")

Results: [1] "GHW BUsh" "Clinton" "Obama"
```

- [ ] potus[-"GW Bush"]
- [ ] potus[1:2 4]
- [x] potus[-3]
- [ ] potus[1,2,4]

#### Q58. A data frame contains two factor -fact1 and fact2- and a numerical outcome variable. Which statement returns results that do NOT include an interaction term?

- [x] anova(lm(outcome ~ fact1 : fact2))
- [ ] anova(lm(outcome ~ fact1 * fact2))
- [ ] anova(lm(outcome ~ fact1 + fact2))
- [ ] anova(lm(outcome ~ fact1 + fact2 + fact1 : fact2))

#### Q59. Review line 1 below. What does the statement on line 2 return?

```r
1 myvect <- c(-2,-1,0)
2 as.logical(myvect)
```

- [ ] [1]-2 -1 0
- [x] [1]TRUE TRUE FALSE
- [ ] [1]FALSE FALSE TRUE
- [ ] [1]NA NA NA
