
from rich.console import Console
from rich.table import Table


console = Console()


table = Table(title="Favorite Movies")
table.add_column("Title", style="cyan")
table.add_column("Release Date", style="magenta")
table.add_column("Box Office", style="green", justify="right")
table.add_row("Flipped", "2010", "$4,325,000")
table.add_row("Spirited Away", "2001", "$355,467,000")
table.add_row("Coco", "2017", "$807,082,196")
console.print(table)


movies = []


while True:
    console.print("\n[bold yellow]Enter your favorite movie details:[/bold yellow]")
    title = input("Movie Title: ")
    release_date = input("Release Date: ")
    box_office = input("Box Office Earnings: ")


    console.print(f"\n[bold cyan]You entered:[/bold cyan] {title}, released in {release_date}, Box Office: {box_office}")


    confirm = input("Is this information correct? (y/n): ")
    if confirm.lower() == 'y':
        movies.append((title, release_date, box_office))
        more = input("Do you want to add more movies? (y/n): ")
        if more.lower() != 'y':
            break
    else:
        console.print("[bold red]Let's re-enter the data.[/bold red]")


with open("movies_data.csv", "w") as file:
    file.write("Title,Release Date,Box Office\n")
    for movie in movies:
        file.write(f"{movie[0]},{movie[1]},{movie[2]}\n")

console.print(f"\n[bold green]Data saved to movies_data.csv![/bold pink]")