library(ggplot2)
df_tot = read.csv("teacherData.csv", header = TRUE, stringsAsFactors = FALSE)

df_pay = read.csv("teacherPayLessons.csv", header = TRUE, stringsAsFactors = FALSE)

#Read individual columns into display dataframe
df_display <-  data.frame(df_tot)
#and name them
colnames(df_display) = c("About Me", 
                         "Me_as_a_Teacher", "My_Lessons_&_Teaching_Style", "URL", "Avg_Rating", "Lessons", "Students",
                         "Lessons_Again", "March", "April", "May", "Unavailable1", "Unavailable2", "Unavailable3", "Unavailable4",
                         "Available1", "Available2", "Available3", "Available4","Booked1","Booked2", "Booked3", "Booked4")
df_display$Lessons = gsub("LESSONS", "", df_display$Lessons)
df_display$Students = gsub("STUDENTS", "", df_display$Students)



#pay information
df_pay %>%
  ggplot(aes(x = Lowest_Rate)) + geom_histogram() +
  xlim(0,45) + scale_x_continuous(labels = scales::dollar, limits = c(0, 45)) +
  ylab("Teacher Count") + xlab("Starting Hourly Rate")



#4 Week Booking Quantities

fourWkBookings = df_display$Booked1 + df_display$Booked2 + df_display$Booked3 + df_display$Booked4
fourwkAvailability = df_display$Available1 + df_display$Available2 + df_display$Available3 + df_display$Available4

#Template Code
#Weight.Loss = c(Low.Calorie, Low.Carb, Low.Fat, Control)

#Tried to get bookings per week, ended up with hourly distribution of bookings
bookedWeeks = c(df_display$Booked1 , df_display$Booked2, df_display$Booked3, df_display$Booked4) #Combining data into
weekCategory = c(rep("Week 1", 369),                    
                 rep("Week 2", 369),                       
                 rep("Week 3", 369),
                 rep("Week 4", 369))

boxplot(bookedWeeks ~ weekCategory,
        col = c("red", "orange", "yellow", "green"),
        main = "Bookings per Week")  

df_display %>%
  ggplot(aes(x= fourWkBookings)) + geom_histogram( ) + 
           xlab(label = "Number of 30 Min Lessons Booked in from June 29 to July 24") +
            xlim(0,250) + ylab("Teacher Count")
      
summary(df_display)
mean(fourWkBookings)
  
#4 week booking rate
df_display %>%
  ggplot(aes(x= bRate)) + 
  geom_histogram(breaks = seq(0, 1, .05) ) + xlab(label = "4 Week Booking Rate") +
  scale_y_continuous(breaks = seq(0, 60, 10)) + ylab("Teacher Count")

bRate = (fourWkBookings/(fourWkBookings+fourwkAvailability))
mean(bRate)

mean(bRate)
df_display %>%
  ggplot(aes(x= Avg_Rating)) + geom_bar() + xlab("Average Rating (out of 5)") + ylab("Teacher Count") +
  xlim(3.5,5) + ylim(0, 90)

#attempt at mean lessons by avg rating
df_display %>%
  filter(Avg_Rating == 5 )# %>%
  summarise( mean(Booking1 + Booking2 + Booking3 + Booking4))


df_display %>%
  ggplot(aes(x= Avg_Rating, y = fourWkBookings )) + geom_point()# + xlab("Average Rating (out of 5)") + ylab("Teacher Count") #+
  #xlim(3.5,5) + ylim(0, 90)

#relationship between students and booking proportion
df_display %>%
  ggplot(aes(x= Students,y = fourWkBookings) ) + geom_point() + scale_x_continuous(breaks = c(2, 4, 6)) +
  ylab(label = "4 Week Booking Rate")

#relationship between lessons booked in May and lessons booked in Julyish
df_display %>%
  #select(Booked1, Booked2, Booked3, Booked4) %>%
  ggplot(aes(x= May,y = fourWkBookings )) + geom_point() + ylab(label = "Number of 30 Min Lessons Booked from June 29 to July 24") +
  xlab(label = "Number of 30 Min Lessons Booked in May")

df_display %>%
  ggplot(aes(x= Lessons ,y = fourWkBookings )) + geom_point() + scale_x_continuous(breaks = 100)

df_display %>%
  #select(Booked1, Booked2, Booked3, Booked4) %>%
  ggplot(aes(x= Students,y = Booked1) ) + geom_point() 

df_display %>%
  #select(Booked1, Booked2, Booked3, Booked4) %>%
  ggplot(aes(x= Lessons,y = Booked1) ) + geom_point() 



WeeklyAvgs = c(mean(df_display$Booked1), mean(df_display$Booked2), mean(df_display$Booked3), mean(df_display$Booked4))

ggplot(weeklyAvgs, aes(x = week))
data(mpg)

library(data.table) 


summary(df_display)