library(shiny)

# Define server logic required to draw a histogram
function(input, output, session) {
  music <- read.csv2("musique.csv")

    output$distPlot <- renderPlot({
      # Extraire les années de la colonne Per
      music$annee <- as.numeric(gsub("s", "", music$Per))
      
      # Filtrer selon les années sélectionnées
      music_filtre <- music[music$annee %in% input$annees, ]
      
      Graph_Annee <- table(music_filtre$Style, music_filtre$annee)

        # Créer un graphique en barres empilées
        barplot(Graph_Annee, 
                col = rainbow(nrow(Graph_Annee)),
                border = 'white',
                beside = TRUE,
                xlab = 'Décennie',
                ylab = 'Nombre de morceaux',
                main = 'Distribution des styles musicaux par décennie',
                legend.text = TRUE,
                args.legend = list(x = "topright", cex = 0.8))
    })

}
