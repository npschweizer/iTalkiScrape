df_tot = read.csv("Data.csv", header = TRUE, stringsAsFactors = FALSE)

df_display <-  data.frame(df_tot$Institution, df_tot$Total.enrollment..fall.2017, df_tot$Revenue.from.tuition.and.fees,
                          df_tot$Spending.on.instruction, df_tot$Tuition.and.fees.revenue.as.percentage.of.all.revenue,
                          df_tot$Type)

colnames(df_display) = c("Institution", "Total Enrollment, Fall 2017", "Revenue from Tuition and Fees",
                         "Spending on Instruction", "Tuition and Fees Revenue as a Percentage of All Revenue",
                         "Type")



library(data.table) 
