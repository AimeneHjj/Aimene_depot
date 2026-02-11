library (tidyr)
library(dplyr)

#chargement des donées
read.csv2("candy.csv")
candy <- read.csv2("candy.csv")
candy

#convertir les colonnes qui ont des points comme séparateur décimaux
candy <- candy %>%
  mutate(across(c(chocolate:win), as.numeric))

#Pivot pour préparer le graphique, rassembler les types de bonbon sur une
#seul et même colonne
candyGraph <- candy %>%
  pivot_longer(cols = c(chocolate, fruity, caramel, peanutalmond, nougat,
                        wafer,hard),
               names_to = "type",
               values_to = "presente") %>%
  filter(presente == 1)  # Garder seulement quand la caractéristique est présente

#####ggplot2
library(ggplot2)
candyGraph %>% #data
drop_na()

candyGraph %>% ggplot()+ #on prépare le mapping
  aes (x=type, fill=type, y=sugar)+ #aesthetic mapping, on établie les liens entre les variable
  geom_boxplot()+ #on rajoute les layers
  
  scale_fill_discrete(palette = "Set3")+
  
  #facet_grid(col=vars(type))+ #facette
  #facet_grid(row=vars(type))+ #facette

  xlab("Type")+ #options
  ylab("sucre")+ #options
  ggtitle("Graphique représentant le taux de sucre par rapport au type de bonbon")+
  
  coord_cartesian() #échelle x et y différente
  #theme(aspect.ratio = 1/2)
