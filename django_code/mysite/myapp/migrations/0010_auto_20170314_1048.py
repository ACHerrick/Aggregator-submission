# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_compare_cuisine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('idd', models.AutoField(primary_key=True, serialize=False)),
                ('cuisine', models.CharField(choices=[('None', '--'), ('Afghan', 'Afghan'), ('African', 'African'), ('Senegalese', 'Senegalese'), ('SouthAfrican', 'South African'), ('American(New)', 'American (New)'), ('American(Traditional)', 'American (Traditional)'), ('Arabian', 'Arabian'), ('Argentine', 'Argentine'), ('Armenian', 'Armenian'), ('AsianFusion', 'Asian Fusion'), ('Australian', 'Australian'), ('Austrian', 'Austrian'), ('Bangladeshi', 'Bangladeshi'), ('Barbeque', 'Barbeque'), ('Basque', 'Basque'), ('Belgian', 'Belgian'), ('Brasseries', 'Brasseries'), ('Brazilian', 'Brazilian'), ('Breakfast&Brunch', 'Breakfast & Brunch'), ('British', 'British'), ('Buffets', 'Buffets'), ('Burgers', 'Burgers'), ('Burmese', 'Burmese'), ('Cafes', 'Cafes'), ('ThemedCafes', 'Themed Cafes'), ('Cafeteria', 'Cafeteria'), ('Cajun/Creole', 'Cajun/Creole'), ('Cambodian', 'Cambodian'), ('Caribbean', 'Caribbean'), ('Dominican', 'Dominican'), ('Haitian', 'Haitian'), ('PuertoRican', 'Puerto Rican'), ('Trinidadian', 'Trinidadian'), ('Catalan', 'Catalan'), ('Cheesesteaks', 'Cheesesteaks'), ('ChickenShop', 'Chicken Shop'), ('ChickenWings', 'Chicken Wings'), ('Chinese', 'Chinese'), ('Cantonese', 'Cantonese'), ('DimSum', 'Dim Sum'), ('Hainan', 'Hainan'), ('Shanghainese', 'Shanghainese'), ('Szechuan', 'Szechuan'), ('ComfortFood', 'Comfort Food'), ('Creperies', 'Creperies'), ('Cuban', 'Cuban'), ('Czech', 'Czech'), ('Delis', 'Delis'), ('Diners', 'Diners'), ('DinnerTheater', 'Dinner Theater'), ('Ethiopian', 'Ethiopian'), ('FastFood', 'Fast Food'), ('Filipino', 'Filipino'), ('Fish&Chips', 'Fish & Chips'), ('Fondue', 'Fondue'), ('FoodCourt', 'Food Court'), ('FoodStands', 'Food Stands'), ('French', 'French'), ('Mauritius', 'Mauritius'), ('Reunion', 'Reunion'), ('Gastropubs', 'Gastropubs'), ('German', 'German'), ('Gluten-Free', 'Gluten-Free'), ('Greek', 'Greek'), ('Guamanian', 'Guamanian'), ('Halal', 'Halal'), ('Hawaiian', 'Hawaiian'), ('Himalayan/Nepalese', 'Himalayan/Nepalese'), ('Honduran', 'Honduran'), ('HongKong Style Cafe', 'Hong Kong Style Cafe'), ('HotDogs', 'Hot Dogs'), ('HotPot', 'Hot Pot'), ('Hungarian', 'Hungarian'), ('Iberian', 'Iberian'), ('Indian', 'Indian'), ('Indonesian', 'Indonesian'), ('Irish', 'Irish'), ('Italian', 'Italian'), ('Calabrian', 'Calabrian'), ('Sardinian', 'Sardinian'), ('Tuscan', 'Tuscan'), ('Japanese', 'Japanese'), ('Conveyor Belt Sushi', 'Conveyor Belt Sushi'), ('Izakaya', 'Izakaya'), ('Japanese Curry', 'Japanese Curry'), ('Ramen', 'Ramen'), ('Teppanyaki', 'Teppanyaki'), ('Kebab', 'Kebab'), ('Korean', 'Korean'), ('Kosher', 'Kosher'), ('Laotian', 'Laotian'), ('LatinAmerican', 'Latin American'), ('Colombian', 'Colombian'), ('Salvadoran', 'Salvadoran'), ('Venezuelan', 'Venezuelan'), ('Live/Raw Food', 'Live/Raw Food'), ('Malaysian', 'Malaysian'), ('Mediterranean', 'Mediterranean'), ('Falafel', 'Falafel'), ('Mexican', 'Mexican'), ('Tacos', 'Tacos'), ('Middle Eastern', 'Middle Eastern'), ('Egyptian', 'Egyptian'), ('Lebanese', 'Lebanese'), ('ModernEuropean', 'Modern European'), ('Mongolian', 'Mongolian'), ('Moroccan', 'Moroccan'), ('NewMexicanCuisine', 'New Mexican Cuisine'), ('Nicaraguan', 'Nicaraguan'), ('Noodles', 'Noodles'), ('Pakistani', 'Pakistani'), ('PanAsian', 'Pan Asian'), ('Persian/Iranian', 'Persian/Iranian'), ('Peruvian', 'Peruvian'), ('Pizza', 'Pizza'), ('Polish', 'Polish'), ('Pop-UpRestaurants', 'Pop-Up Restaurants'), ('Portuguese', 'Portuguese'), ('Poutineries', 'Poutineries'), ('Russian', 'Russian'), ('Salad', 'Salad'), ('Sandwiches', 'Sandwiches'), ('Scandinavian', 'Scandinavian'), ('Scottish', 'Scottish'), ('Seafood', 'Seafood'), ('Singaporean', 'Singaporean'), ('Slovakian', 'Slovakian'), ('SoulFood', 'Soul Food'), ('Soup', 'Soup'), ('Southern', 'Southern'), ('Spanish', 'Spanish'), ('SriLankan', 'Sri Lankan'), ('Steakhouses', 'Steakhouses'), ('SupperClubs', 'Supper Clubs'), ('SushiBars', 'Sushi Bars'), ('Syrian', 'Syrian'), ('Taiwanese', 'Taiwanese'), ('TapasBars', 'Tapas Bars'), ('Tapas/Small Plates', 'Tapas/Small Plates'), ('Tex-Mex', 'Tex-Mex'), ('Thai', 'Thai'), ('Turkish', 'Turkish'), ('Ukrainian', 'Ukrainian'), ('Uzbek', 'Uzbek'), ('Vegan', 'Vegan'), ('Vegetarian', 'Vegetarian'), ('Vietnamese', 'Vietnamese'), ('Waffles', 'Waffles'), ('Wraps', 'Wraps')], default='Waffle', max_length=100, verbose_name='To find top city for a cuisine, choose cuisine here:')),
            ],
        ),
        migrations.AlterField(
            model_name='compare',
            name='cuisine',
            field=models.CharField(choices=[('None', '--'), ('Afghan', 'Afghan'), ('African', 'African'), ('Senegalese', 'Senegalese'), ('SouthAfrican', 'South African'), ('American(New)', 'American (New)'), ('American(Traditional)', 'American (Traditional)'), ('Arabian', 'Arabian'), ('Argentine', 'Argentine'), ('Armenian', 'Armenian'), ('AsianFusion', 'Asian Fusion'), ('Australian', 'Australian'), ('Austrian', 'Austrian'), ('Bangladeshi', 'Bangladeshi'), ('Barbeque', 'Barbeque'), ('Basque', 'Basque'), ('Belgian', 'Belgian'), ('Brasseries', 'Brasseries'), ('Brazilian', 'Brazilian'), ('Breakfast&Brunch', 'Breakfast & Brunch'), ('British', 'British'), ('Buffets', 'Buffets'), ('Burgers', 'Burgers'), ('Burmese', 'Burmese'), ('Cafes', 'Cafes'), ('ThemedCafes', 'Themed Cafes'), ('Cafeteria', 'Cafeteria'), ('Cajun/Creole', 'Cajun/Creole'), ('Cambodian', 'Cambodian'), ('Caribbean', 'Caribbean'), ('Dominican', 'Dominican'), ('Haitian', 'Haitian'), ('PuertoRican', 'Puerto Rican'), ('Trinidadian', 'Trinidadian'), ('Catalan', 'Catalan'), ('Cheesesteaks', 'Cheesesteaks'), ('ChickenShop', 'Chicken Shop'), ('ChickenWings', 'Chicken Wings'), ('Chinese', 'Chinese'), ('Cantonese', 'Cantonese'), ('DimSum', 'Dim Sum'), ('Hainan', 'Hainan'), ('Shanghainese', 'Shanghainese'), ('Szechuan', 'Szechuan'), ('ComfortFood', 'Comfort Food'), ('Creperies', 'Creperies'), ('Cuban', 'Cuban'), ('Czech', 'Czech'), ('Delis', 'Delis'), ('Diners', 'Diners'), ('DinnerTheater', 'Dinner Theater'), ('Ethiopian', 'Ethiopian'), ('FastFood', 'Fast Food'), ('Filipino', 'Filipino'), ('Fish&Chips', 'Fish & Chips'), ('Fondue', 'Fondue'), ('FoodCourt', 'Food Court'), ('FoodStands', 'Food Stands'), ('French', 'French'), ('Mauritius', 'Mauritius'), ('Reunion', 'Reunion'), ('Gastropubs', 'Gastropubs'), ('German', 'German'), ('Gluten-Free', 'Gluten-Free'), ('Greek', 'Greek'), ('Guamanian', 'Guamanian'), ('Halal', 'Halal'), ('Hawaiian', 'Hawaiian'), ('Himalayan/Nepalese', 'Himalayan/Nepalese'), ('Honduran', 'Honduran'), ('HongKong Style Cafe', 'Hong Kong Style Cafe'), ('HotDogs', 'Hot Dogs'), ('HotPot', 'Hot Pot'), ('Hungarian', 'Hungarian'), ('Iberian', 'Iberian'), ('Indian', 'Indian'), ('Indonesian', 'Indonesian'), ('Irish', 'Irish'), ('Italian', 'Italian'), ('Calabrian', 'Calabrian'), ('Sardinian', 'Sardinian'), ('Tuscan', 'Tuscan'), ('Japanese', 'Japanese'), ('Conveyor Belt Sushi', 'Conveyor Belt Sushi'), ('Izakaya', 'Izakaya'), ('Japanese Curry', 'Japanese Curry'), ('Ramen', 'Ramen'), ('Teppanyaki', 'Teppanyaki'), ('Kebab', 'Kebab'), ('Korean', 'Korean'), ('Kosher', 'Kosher'), ('Laotian', 'Laotian'), ('LatinAmerican', 'Latin American'), ('Colombian', 'Colombian'), ('Salvadoran', 'Salvadoran'), ('Venezuelan', 'Venezuelan'), ('Live/Raw Food', 'Live/Raw Food'), ('Malaysian', 'Malaysian'), ('Mediterranean', 'Mediterranean'), ('Falafel', 'Falafel'), ('Mexican', 'Mexican'), ('Tacos', 'Tacos'), ('Middle Eastern', 'Middle Eastern'), ('Egyptian', 'Egyptian'), ('Lebanese', 'Lebanese'), ('ModernEuropean', 'Modern European'), ('Mongolian', 'Mongolian'), ('Moroccan', 'Moroccan'), ('NewMexicanCuisine', 'New Mexican Cuisine'), ('Nicaraguan', 'Nicaraguan'), ('Noodles', 'Noodles'), ('Pakistani', 'Pakistani'), ('PanAsian', 'Pan Asian'), ('Persian/Iranian', 'Persian/Iranian'), ('Peruvian', 'Peruvian'), ('Pizza', 'Pizza'), ('Polish', 'Polish'), ('Pop-UpRestaurants', 'Pop-Up Restaurants'), ('Portuguese', 'Portuguese'), ('Poutineries', 'Poutineries'), ('Russian', 'Russian'), ('Salad', 'Salad'), ('Sandwiches', 'Sandwiches'), ('Scandinavian', 'Scandinavian'), ('Scottish', 'Scottish'), ('Seafood', 'Seafood'), ('Singaporean', 'Singaporean'), ('Slovakian', 'Slovakian'), ('SoulFood', 'Soul Food'), ('Soup', 'Soup'), ('Southern', 'Southern'), ('Spanish', 'Spanish'), ('SriLankan', 'Sri Lankan'), ('Steakhouses', 'Steakhouses'), ('SupperClubs', 'Supper Clubs'), ('SushiBars', 'Sushi Bars'), ('Syrian', 'Syrian'), ('Taiwanese', 'Taiwanese'), ('TapasBars', 'Tapas Bars'), ('Tapas/Small Plates', 'Tapas/Small Plates'), ('Tex-Mex', 'Tex-Mex'), ('Thai', 'Thai'), ('Turkish', 'Turkish'), ('Ukrainian', 'Ukrainian'), ('Uzbek', 'Uzbek'), ('Vegan', 'Vegan'), ('Vegetarian', 'Vegetarian'), ('Vietnamese', 'Vietnamese'), ('Waffles', 'Waffles'), ('Wraps', 'Wraps')], default='Waffle', max_length=100, verbose_name='If you would like to specify a cuisine for comparison, choose here:'),
        ),
    ]
