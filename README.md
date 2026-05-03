# Gerador de Senhas Seguras

## Projeto de Pós-Graduação em Generative AI (GenAI)

### Autor

Mario Correa Rodrigues Junior

### Tecnologia Principal

* Python 3.13+
* Click (CLI)
* Pytest (Testes Automatizados)
* Git/GitHub (Versionamento)

---

# Descrição Acadêmica do Projeto

O **Gerador de Senhas Seguras** é uma aplicação desenvolvida em Python com interface de linha de comando (CLI), projetada para gerar senhas robustas e aleatórias com base em critérios configuráveis pelo usuário.

O sistema permite personalização completa da senha por meio da definição de:

* Comprimento da senha
* Inclusão de letras maiúsculas
* Inclusão de letras minúsculas
* Inclusão de números
* Inclusão de caracteres especiais

---

# Objetivos do Projeto

## Objetivo Geral

Desenvolver uma solução segura e profissional para geração automatizada de senhas fortes.

## Objetivos Específicos

* Implementar geração randômica segura utilizando Python
* Construir interface CLI utilizando Click
* Aplicar arquitetura modular baseada em pacotes
* Desenvolver testes automatizados para validação funcional
* Aplicar versionamento com Git/GitHub
* Produzir documentação técnica e acadêmica

---

# Arquitetura do Projeto

```txt
gerador-senhas-seguras/
│
├── src/
│   └── password_generator/
│       ├── __init__.py
│       ├── generator.py
│       └── cli.py
│
├── tests/
│   └── test_generator.py
│
├── venv/
├── .gitignore
├── pytest.ini
├── requirements.txt
├── README.md
└── setup.py
```

---

# Funcionamento Técnico

## Módulo Principal (`generator.py`)

Responsável pela lógica de geração segura de senhas utilizando:

* `secrets.choice()` para maior segurança criptográfica
* Biblioteca `string` para composição dinâmica de conjuntos de caracteres

### Critérios suportados:

* Uppercase
* Lowercase
* Dígitos
* Símbolos especiais

---

## Interface CLI (`cli.py`)

Desenvolvida com Click, permite execução parametrizada:

### Exemplo:

```bash
python -m src.password_generator.cli --length 16 --uppercase --lowercase --numbers --special
```

---

# Requisitos do Sistema

## Software necessário:

* Python 3.11+
* Git
* Visual Studio Code (ou Visual Studio com suporte Python)

---

# Instalação e Configuração Local

## 1. Clonar repositório

```bash
git clone https://github.com/MarioJr7/gerador-senhas-seguras.git
cd gerador-senhas-seguras
```

---

## 2. Criar ambiente virtual

```bash
python -m venv venv
```

### Ativação:

### Windows:

```bash
venv\Scripts\activate
```

### Linux/Mac:

```bash
source venv/bin/activate
```

---

## 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

# Execução do Projeto

## Comando padrão:

```bash
python -m src.password_generator.cli --length 16 --uppercase --lowercase --numbers --special
```

---

## Exemplos:

### Senha de 20 caracteres:

```bash
python -m src.password_generator.cli --length 20
```

### Sem caracteres especiais:

```bash
python -m src.password_generator.cli --length 12 --no-special
```

### Apenas números:

```bash
python -m src.password_generator.cli --length 8 --no-uppercase --no-lowercase --numbers --no-special
```

---

# Exemplo de Saída Esperada

```bash
Senha gerada: 9@Kx!Lm2#PqRs7$Ab
```

---

# Testes Automatizados

## Execução:

```bash
pytest
```

## Testes implementados:

* Comprimento correto
* Presença de letras maiúsculas
* Presença de números
* Validação de critérios inválidos

---

# Exemplo de Resultado:

```bash
4 passed in 0.15s
```

---

# Segurança Aplicada

## Boas práticas implementadas:

* Uso de `secrets` para segurança criptográfica
* Estrutura modular
* Separação entre lógica e interface
* Testes automatizados
* Controle de dependências

---

# Potenciais Melhorias Futuras

## Expansão técnica:

* Interface Web com Flask ou FastAPI
* Dockerização
* CI/CD com GitHub Actions
* API REST
* Indicador de força de senha
* Integração com IA para análise de segurança

---

# Contribuição Acadêmica

Este projeto demonstra competências em:

* Desenvolvimento seguro
* Arquitetura de software
* Engenharia de testes
* Automação
* Documentação técnica
* Gestão de versões

---

# Licença

Projeto acadêmico desenvolvido para fins educacionais e de pesquisa.

---

# Conclusão

O **Gerador de Senhas Seguras** representa uma implementação prática de conceitos fundamentais de segurança digital, desenvolvimento Python e engenharia de software, servindo como base sólida para aplicações futuras em:

* Cybersecurity
* DevSecOps
* Ferramentas corporativas
* Aplicações GenAI com foco em segurança

---

# Contato

Para fins acadêmicos ou profissionais, utilize este repositório como base para expansão e melhorias futuras.
