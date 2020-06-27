library(shiny)
source("global.R")
library(googleVis)
fluidPage( 
  titlePanel("Higher Education Instructional Expenditure"),
  sidebarLayout(
    sidebarPanel(
      selectizeInput(inputId = "Type",
                     label = "Institution Type",
                     choices = unique(df_tot$Type)),
      width = 2
    ),
    mainPanel(tabsetPanel(#flowLayout(
      tabPanel(
        "Aggregate Spending and Revenue Dynamics",
        br(),
        print(h4("As a group, only 8% of private institutions spent more than they received 
                 in tuition and fees, compared to 79% of public institutions. The median public 
                 institution spending $1.33 on instruction for every dollar in tuition and fees, while 
                 the median private institution spent only $.59 for the same dollar. It is important 
                 to note that this is not necessarily a consequence of increased non-instructional 
                 spending on the part of private institutions, since state institutions tend to draw 
                 substantial resources from state governments to supplement their budgets which is 
                 unavailable to private institutions.")),
        fluidRow(column(
          width = 4, plotOutput("SpendExceedTuitionPie")
        ), #Pie Chart, Proportion of Institutions Where Spending Exceeds Tuition Revenue
        column(width = 8, plotOutput(
          "SpendRevRatioDist"
        )), #Distribution, Distribution of Instructional Spending To Tuition Revenue Ratios),
        fluidRow(column(
          width = 12,
          br(),
          print(h4(
          "In general, institutions that derived a lower proportion of revenue from tuition and fees 
          spent more on instruction relative to tuition and fee revenue. Among institutions that derived 
          less than 25% of their total revenue from tuition and fees, the median spending on instruction 
          was $3,214 more than tuition revenue per student.  However, in institutions that derived more than 
          75% of revenue from tuition and fees, median per student tuition and fee revenue exceeded revenue by 
          $8,323. Whereas 93% institutions that derived less than 25% of their total revenue from tuition and fees 
          spent more on instruction than they received in tuition revenue, no institutions that derived more
          than 75% of their revenue from tuition and fees spent more on instruction than they received in revenue.")),
          plotlyOutput("SpendRevDiffOverRevPerScatter")
        #  verbatimTextOutput("info")
        ) #Scatter Plot, Mapping of Difference in Between Revenue and Spending against Tuition as Percentage of Revenue)
        ))),
     tabPanel(
       "Spending & Revenue Dynamics Per Students",
       
       fluidRow(
         column(
           print("Variation in instructional spending is relatively limited, with public institutions spending
                 a median of $10,640 per student and private institutinos spending a median of $8,824 per student
                 on instruction, respectively. The biggest public and private spenders, University of Texas Southwestern Medical Center
                 at Dallas and Weill Cornell Medicine, spent $455,129.64 and $198,199.62 per student on instruction,
                 respectively."),
           width = 5, plotOutput("SpendingPerStudent")),
           column(
             print("But variation in revenue from tuition and fees per student was much greater, with public institutions
                   bringing in a median of $5,451 and private institutions bringing in a median of $14,741 in tuition and
                   fee revenue per student, respectively."),
             width = 5, plotOutput("RevenuePerStudent")
           ),
         fluidRow(
           column(
             width=12, plotOutput("SpendingvsRevenue")
           )
         )
         )
       ),
     
     tabPanel(
       "Data",
       fluidRow(DT::dataTableOutput("table"))
     ),
     tabPanel(
       "Notes",
       print(h1("Notes")),
             print(h4("Dataset derived from analysis of Department of Education data performed
                by the Chronicle of Higher Education. To access the dataset, visit 
                      https://www.chronicle.com/article/Colleges-That-Spent-Far-Less/246669.
                      Data can also be accessed through the Department of Education at 
                      https://nces.ed.gov/ipeds/use-the-data."
                      )),
            print(h4("All revenue and expenditure amounts are for 2016-2017. Data cover 
                     degree-granting four-year public and private institutions in the 
                     United States that are eligible to participate in Title IV financial-aid 
                     programs and that had at least 500 students enrolled in the fall of 2017.
                     Tuition and fees excludes room and board. Intruction costs do not included expenses
                     categorized as academic support, such as academic administration 
                     and course development. For more information on the dataset visit
                     https://www.chronicle.com/article/Colleges-That-Spent-Far-Less/246669."
              
            )),
       print(h4("'Revenue' indicates funds derived from the payment of tuition and fees on an 
                aggregate or per student basis as noted. 'Spending' indicates funds expended
                on instructional costs on aggregate or per student basis, as noted."
                
       ))
     )
     )
     ) 
    )
    
    )
  

    