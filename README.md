# Guestbook AWS – Proof of Concept

Questo repository contiene un **piccolo progetto di studio** realizzato come Proof of Concept per fare pratica con il deploy di un’applicazione **full stack con database** su AWS.

L’obiettivo non era creare un prodotto finito, ma **capire cosa significa portare online un’applicazione reale**, usando risorse cloud e affrontando problemi concreti.

## Cosa fa il progetto
Una semplice applicazione tipo *guestbook*:
- frontend web
- backend che gestisce i dati
- database relazionale
- applicazione accessibile pubblicamente

👉 Live demo:  
http://guestbook-alb-1125737450.us-east-1.elb.amazonaws.com

## Tech stack
- Backend: Flask + SQLAlchemy
- Frontend: HTML + Jinja2
- Database: MySQL (RDS)
- Infrastruttura: AWS (EC2, ALB, VPC, Security Groups)
- Deploy: manuale via AWS CLI e console

## Perché questo progetto
Questo PoC fa parte di un **percorso di test e apprendimento** con l’obiettivo di arrivare a sviluppare un **vero sito web full stack con database**, gestendo anche la parte infrastrutturale.

Il focus è stato su:
- collegare correttamente frontend, backend e database
- configurare l’infrastruttura cloud
- capire errori e limiti reali del Free Tier

## Stato del progetto
- funzionante
- volutamente semplice
- non pensato per produzione

## Possibili evoluzioni (v2)
- HTTPS con dominio e ACM
- Infrastructure as Code (Terraform / CloudFormation)
- multi-AZ
- refactoring del deploy

Per dettagli sugli errori incontrati e sulle scelte fatte, vedere `notes.md`.
