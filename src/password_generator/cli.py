import click
from src.password_generator.generator import generate_password


@click.command()
@click.option('--length', default=12, help='Tamanho da senha')
@click.option('--uppercase/--no-uppercase', default=True)
@click.option('--lowercase/--no-lowercase', default=True)
@click.option('--numbers/--no-numbers', default=True)
@click.option('--special/--no-special', default=True)
def main(length, uppercase, lowercase, numbers, special):
    password = generate_password(
        length=length,
        uppercase=uppercase,
        lowercase=lowercase,
        numbers=numbers,
        special=special
    )

    click.echo(f"Senha gerada: {password}")


if __name__ == '__main__':
    main()