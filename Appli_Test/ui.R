library(shiny)

# Define UI for application that draws a histogram
fluidPage(

    # Application title
    titlePanel("Distribution des styles musicaux"),

    # Sidebar with a slider input for number of bins
    sidebarLayout(
        sidebarPanel(
          checkboxGroupInput("annees",
                        "Choisir les décennies:",
                        choices = c("70s" = "70",
                                    "80s" = "80",
                                    "90s" = "90"),
                        selected = c("70", "80", "90"))
        ),

        # Show a plot of the generated distribution
        mainPanel(
            plotOutput("distPlot")
        )
    )
)
