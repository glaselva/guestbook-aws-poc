# Notes di progetto – Guestbook AWS PoC

Queste note descrivono **come è stato realizzato il progetto** e cosa è andato storto durante il deploy.

## Modalità di lavoro
- Infrastruttura creata **manualmente**
- Uso di **AWS CLI e console**
- Nessun Infrastructure as Code
- Obiettivo: capire i concetti, non automatizzare

## Architettura (semplificata)
- Application Load Balancer (HTTP)
- EC2 t3.micro con Flask
- RDS MySQL (Free Tier)
- Security Groups con regole dedicate
- VPC con subnet pubbliche

## Problemi incontrati

### HTTPS sull’ALB
- Tentativo iniziale di configurare HTTPS
- ACM richiede un **dominio personalizzato**
- Il dominio non è incluso nel Free Tier
- Scelta finale: **HTTP only** per restare a costo zero

### HTTP 503
- L’ALB restituiva errori 503
- Causa: target group configurato su Availability Zone diverse da quella dell’EC2
- Risoluzione: allineamento corretto delle AZ

Errore semplice, ma istruttivo.

## Cosa ho imparato
- Il cloud non perdona configurazioni imprecise
- Gli errori di rete sono più frequenti del codice rotto
- Fare deploy reale è molto diverso dai tutorial
- Capire *perché* qualcosa non funziona è la parte più formativa

## Considerazioni finali
Questo progetto non punta a mostrare codice complesso, ma:
- capacità di portare un’applicazione online
- comprensione dei componenti cloud di base
- approccio pratico e iterativo

La versione successiva sarà orientata all’automazione e alla pulizia dell’infrastruttura.
