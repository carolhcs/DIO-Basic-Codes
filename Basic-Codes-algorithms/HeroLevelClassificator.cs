using System;

public class HeroLevelClassificator
{
    public static void Main(string[] args)
    {
        string heroName = "";
        int heroXP = 0;
        string heroLevel = "";

        Console.WriteLine("/n Enter with your hero name: ");
        heroName = Console.ReadLine();
        Console.WriteLine("/n Enter with your hero experience: ");
        heroLevel = Console.ReadLine();

        heroXP = int.Parse(heroLevel);

        if (heroXP <= 1000)
        {
            heroLevel = "Ferro";
        }
        else if (heroXP <= 2000)
        {
            heroLevel = "Bronze";
        }
        else if (heroXP <= 5000)
        {
            heroLevel = "Prata";
        }
        else if (heroXP <= 7000)
        {
            heroLevel = "Ouro";
        }
        else if (heroXP <= 8000)
        {
            heroLevel = "Platina";
        }
        else if (heroXP <= 9000)
        {
            heroLevel = "Ascendente";
        }
        else if (heroXP <= 10000)
        {
            heroLevel = "Imortal";
        }
        else
        {
            heroLevel = "Radiante";
        }

        Console.WriteLine($"O Heroi de nome {heroName} está no nivel de {heroLevel}");
    }
}
