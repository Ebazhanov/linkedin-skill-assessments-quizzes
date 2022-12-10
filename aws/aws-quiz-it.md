## Amazon Web Services (AWS)

#### D1. Hai un'applicazione che utilizza un database MySQL da 100 GB di cui stai eseguendo la migrazione in AWS. Cosa dovresti considerare quando decidi se ospitare il database su RDS per MySQL o Aurora?

- \[ ] costo
- \[ ] facilità di manutenzione vs. granularità del controllo
- \[x] tutte queste risposte
- \[ ] l'attuale motore di archiviazione utilizzato dall'applicazione, ad esempio InnoDB o MyISAM

#### D2. Quale database è un tipo di database NoSQL in grado di archiviare e recuperare rapidamente coppie chiave-valore?

- \[ ] Aurora
- \[ ] Nettuno
- \[ ] RDS per MySQL
- \[x] DynamoDB

#### D3. Il database è un'istanza RDS che esegue SQL Server con replica Multi-AZ e sono disponibili diverse utilità console .NET meno recenti che eseguono operazioni di database ogni 15 secondi. Quando il cluster deve passare dal server di database primario all'autorità di disponibilità secondaria, le utilità .NET iniziano a segnalare errori di connessione al database, sebbene altre applicazioni siano in grado di accedere al database. Come si corregge questo problema?

- \[ ] Utilizzare la console RDS per forzare il riavvio dell'istanza del database in modo che il server primario diventi nuovamente il server master.
- \[ ] Il server che esegue le utilità .NET memorizza nella cache la ricerca DNS nell'indirizzo del cluster di database. Svuotare la cache DNS del server e forzare le utilità C# ad aprire nuove connessioni al database.
- \[ ] A.NET applicazione conserverà l'indirizzo IP di una stringa di connessione fino al riavvio della macchina host.
- \[x] Le utilità NET devono modificare l'endpoint SQL Server nelle stringhe di connessione per leggerle dal server di database secondario utilizzando un try/catch.

#### D4. Quali servizi AWS possono aiutarti ad automatizzare la pipeline di sviluppo per l'integrazione continua e la distribuzione continua?

- \[ ] CodePipeline
- \[ ] CodeDeploy
- \[x] tutte queste risposte
- \[ ] CodeBuild

#### D5. Quale servizio AWS è conforme agli standard descritti in Payment Card Industry Data Security Standard (PCI DSS) Level 1 per la gestione e la trasmissione dei dati delle carte di credito?

- \[ ] Gateway API
- \[x] tutte queste risposte
- \[ ] Servizio di coda semplice (SQS)
- \[ ] Flussi di dati Kinesis

#### D6. Nel tuo array di archiviazione collegato alla rete sono presenti una grande quantità di file che devono essere archiviati e mantenuti per un periodo di 10 anni a causa delle normative del settore. Questi dati saranno accessibili raramente, ma devono essere conservati Qual è il miglior servizio AWS per l'archiviazione di questi dati?

- \[ ] EFS
- \[ ] Palla di neve
- \[ ] OEBS
- \[x] Ghiacciaio S3

#### D7. Per il tuo account root AWS, hai generato una password casuale della lunghezza massima consentita e hai incluso caratteri speciali. Quali passaggi aggiuntivi è necessario eseguire per proteggere l'account root AWS?

- \[ ] Creare un ruolo AM per l'amministratore dell'account con i privilegi più elevati. Non memorizzare la password di root, ma quando è necessario l'account root reimpostare la password sull'account root tramite e-mail di conferma e ripetere questa procedura.
- \[ ] Archivia la tua password generata casualmente nel tuo database dei segreti organizzativi utilizzando un servizio come 1Password o LastPass e concedi l'accesso a questo segreto solo al team DevOps.
- \[ ] Crea account IAM per i tuoi amministratori e collega la policy AdministratorAccess ai loro account. Disabilita l'account root nelle impostazioni utente.
- \[x] Crea un ruolo IAM per l'amministratore dell'account con i privilegi più alti e non utilizzare l'account root nelle operazioni quotidiane. Abilitare l'autenticazione a due fattori sull'account root

#### D8. Quale opzione elastica di bilanciamento del carico supporta Lambda come destinazione?

- \[ ] Network Load Balancer
- \[ ] Lambda non può essere chiamato direttamente dalle richieste web in arrivo. È necessario utilizzare API Gateway.
- \[ ] Bilanciamento del carico classico
- \[x] Application Load Balancer

#### D9. In che modo è possibile progettare una soluzione per un database SQL Server da replicare tra le regioni AWS in un'architettura attivo-attiva?

- \[ ] Utilizzare RDS per SQL Server e creare la stessa istanza in due aree diverse. Utilizzare Servizio migrazione database per mantenere sincronizzato ogni database.
- \[ ] Utilizzare un peering VPN o VPC per stabilire una connessione tra i VPC in ogni regione. Installa SQL Server Enterprise Edition nelle istanze EC2 in ogni area geografica e configura un gruppo di disponibilità Sempre attivo.
- \[x] Utilizzare RDS per SQL Server 2016 o 2017 Enterprise Edition. Abilitare il supporto Multi-AZ e selezionare l'opzione Mirroring/Always On. Selezionare un'altra regione per l'opzione di mirroring.
- \[ ] Non è possibile impostare un'architettura attivo-attiva per SQL Server che si estende su aree geografiche.

[Riferimento](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html?opt_id=oeu1612780272452r0.9199525073583283)

#### D10. Quanto costa lanciare un'istanza EC2 da AWS Marketplace?

- \[ ] Tutte le immagini in AWS Marketplace comportano costi orari aggiuntivi oltre ai costi derivanti dalla dimensione dell'istanza selezionata.
- \[ ] Puoi avviare solo immagini create da altri utenti sul tuo account AWS, quindi paghi solo per le dimensioni dell'istanza selezionata e i costi di storage S3 per l'immagine di base.
- \[x] Ogni immagine ha i propri prezzi che potrebbero essere gratuiti o includere addebiti per i costi di licenza del software. Pagherai anche per l'istanza su cui viene eseguita l'immagine
- \[ ] Tutte le immagini in AWS Marketplace contengono solo software open source senza costi aggiuntivi e sono create da altri utenti AWS. Pagherai solo per la dimensione dell'istanza selezionata.

#### D11. Quando si utilizza un cluster ECS con istanze EC2, quali attività di manutenzione è necessario eseguire sugli EC2?

- \[ ] Le istanze create da ECS non hanno patch che devono essere applicate; tuttavia, è necessario assicurarsi che i contenitori contengano aggiornamenti della protezione importanti.
- \[x] Aggiornare il cluster con istanze create dall'AMI ECS più recente.
- \[ ] I cluster ECS non utilizzano istanze EC2.
- \[ ] Non devi manipolare direttamente le istanze EC2 create da ECS. AWS aggiornerà automaticamente queste istanze.

#### D12. Quale server di memorizzazione nella cache in memoria non è supportato da ElastiCache?

- \[ ] Redis 5
- \[ ] Memcached
- \[x] Elasticsearch
- \[ ] Redis 3

#### D13. Quale servizio AWS può essere utilizzato per generare la documentazione richiesta da vari standard di conformità, come payment card industry data security standard (PCI DSS) livello 1 per la gestione dei dati delle carte di credito?

- \[x] Artefatto
- \[ ] DocumentDB
- \[ ] Stampa il riepilogo della conformità AWS e conservalo con la documentazione richiesta per un audit.
- \[ ] Gestore dei segreti

#### D14. Quando si utilizza AWS per la ricerca e lo sviluppo prima di una migrazione pianificata, come si evitano aumenti o picchi imprevisti nella fatturazione?

- \[ ] Utilizza la dashboard di fatturazione per creare un budget di costo. Inserisci l'importo massimo che desideri venga addebitato ogni mese. Eventuali addebiti superiori a questo importo causeranno la sospensione automatica di tali risorse da parte di AWS
- \[ ] Utilizzando l'account AWS root, attiva l'accesso IAM alle informazioni di fatturazione per l'account. Assicurati che i tuoi utenti IAM dispongano della policy Billing FullAccessGroup. Quindi, dalla dashboard di fatturazione, controlla gli addebiti maturati una volta al giorno.
- \[ ] Se utilizzi il piano gratuito di AWS, dovrai confermare l'utilizzo di qualsiasi servizio che superi i limiti del piano gratuito di AWS.
- \[x] Utilizzando l'account AWS root abilita gli avvisi di fatturazione nelle preferenze dell'utente. Quindi usa CloudWatch per creare un allarme di fatturazione e impostare una soglia su un importo in dollari specifico per i costi mensili stimati.

#### D15. Stai creando una tabella DynamoDB per archiviare tutti i film che sono stati rilasciati dal 1938. La tua applicazione consentirà agli utenti di cercare per titolo del film e vedere i dettagli di quel film. Dato l'esempio seguente che mostra i dati del filmato che verranno importati, qual è il miglior set di chiavi da applicare a questa tabella?

```json
{
  "title": "The Avengers",
  "year": 2012,
  "cast": ["Mark Ruffalo", "Robert Downey, Jr."],
  "genres": ["Action"]
}
```

- \[ ] La chiave primaria deve essere una chiave di partizione del campo del titolo.
- \[ ] La chiave primaria dovrebbe essere il campo del titolo e la chiave di partizione dovrebbe essere il campo dei generi.
- \[ ] La chiave primaria dovrebbe essere una chiave composita composta da una chiave di partizione nel campo del titolo e una chiave di ordinamento nel campo dell'anno.
- \[x] La chiave primaria deve essere creata come un valore completamente univoco, ad esempio un elenco numerico sequenziale di ID filmato. La chiave di partizione dovrebbe essere il campo title per una ricerca rapida.

#### D16. Quale archivio dati offre un modo semplice e rapido per archiviare gli attributi utente di base in un formato basato su oggetti?

- \[ ] ORDS per Oracle
- \[ ] Redshift
- \[ ] Nettuno
- \[x] DynamoDB

#### D17. È necessario un database senza schema. Quale servizio di database Amazon fornisce tale soluzione?

- \[ ] ORDS
- \[ ] Aurora
- \[ ] Redshift
- \[x] DynamoDB

#### D18. Quale canale di comunicazione SNS non supporta in modo nativo?

- \[ ] Messaggio di testo OSMS
- \[ ] notifica push
- \[ ] e-mail
- \[x] telefonata automatica

#### D19. Quando si progetta un'applicazione Web serverless utilizzando Lambda, quale concetto chiave è necessario prendere in considerazione nel progetto?

- \[ ] Le applicazioni Web serverless vengono eseguite all'interno del browser Web dell'utente, quindi sarà necessario archiviare tutti i dati che l'utente modifica direttamente in un database.
- \[ ] Lambda consente solo di scrivere funzioni in JavaScript.
- \[ ] Lambda non utilizza server, quindi può solo restituire la stessa richiesta a ogni utente.
- \[x] Lambda è senza stato, quindi non ricorderà chi è un utente tra una richiesta e l'altra.

#### D20. Un principio di DevOps è quello di visualizzare l'infrastruttura come codice. Quale servizio AWS ti consente di creare script per la tua infrastruttura AWS?

- \[ ] CloudTrail
- \[x] CloudFormation
- \[ ] AWS Config
- \[ ] Catalogo dei servizi AWS

#### D21. È stata creata un'istanza di Windows EC2 con un indirizzo IP pubblico e installato SQL Server. Quando si tenta di connettersi a SQL Server da SQL Server Enterprise Manager nel computer locale, l'istanza di Windows EC2 non è in grado di stabilire una connessione al server. Qual è la prima cosa che dovresti controllare?

- \[ ] Controllare le tabelle di routing per il VPC.
- \[x] Verificare che i gruppi di sicurezza assegnati consentano il traffico della porta TCP 1433 dall'indirizzo IP corrente.
- \[ ] Controllare i criteri all'interno di Windows Firewall.
- \[ ] Verificare che ci si stia connettendo all'istanza utilizzando un utente che non è sa.

#### D22. Si sta ospitando un'applicazione configurata per lo streaming di contenuti multimediali ai client sulle porte TCP 3380-3384, 3386-3388 e 3390. La scheda In ingresso riportata di seguito mostra tre criteri di gruppo di sicurezza in ingresso associati a questa istanza. Quale criterio dovresti usare?

![image](images/001.png?raw=png)

- \[x] La regola che espone le porte TCP 3380-3390 esporrebbe pubblicamente anche la porta 3389 (RDP) all'intera Internet. Scrivere regole separate per esporre solo le porte necessarie.
- \[ ] La prima regola del gruppo di sicurezza consente tutto il traffico in questa istanza. L'esposizione dell'intera istanza all'intera Internet lascia il server aperto a vari attacchi degli altri servizi in esecuzione su numeri di porta diversi.
- \[ ] Verifica che i proprietari degli account AWS controllino effettivamente l'intero blocco CIDR C per 12.228.11.0-255 e che si tratti di IP protetti per l'accesso RDP in questa istanza.
- \[ ] Non ci sono raccomandazioni da fare.

#### D23. Hai quattro server Web front-end dietro un servizio di bilanciamento del carico, che utilizzano NFS per accedere a un'altra istanza EC2 che ridimensiona e archivia le immagini per l'applicazione front-end. Quali criteri di gruppo di sicurezza devono essere assegnati a questi server?

- \[ ] Assegna IP elastici a tutte le istanze e crea un gruppo che consenta a tutto il traffico di passare tra ciascuna delle cinque
  Indirizzi IP elastici e consentono tutto il traffico HTTPS in entrata.
- \[x] I server Web front-end devono consentire HTTPS. Assegnare un altro gruppo a tutte le istanze che consenta a tutto il traffico di passare tra le istanze utilizzando tale gruppo.
- \[ ] Creare un gruppo di sicurezza che consenta il traffico NFS, HTTP e HTTPS in ingresso da tutti gli indirizzi IP. Applicare questo gruppo a tutti i server.
- \[ ] Creare un gruppo di sicurezza che consenta il traffico HTTP e HTTPS in ingresso da tutti gli indirizzi IP e applicarlo ai server Web. Creare un secondo gruppo di sicurezza per l'archivio file NFS che consenta il traffico NFS in uscita verso l'intervallo IP privato dei server Web front-end.

#### D24. Hai un server web Linux EC2 che improvvisamente sta scadendo su tutte le richieste HTTP e i tuoi tentativi di connessione SSH stanno scadendo. Si nota che non riesce il controllo dello stato del sistema nella console EC2. Quali azioni dovresti intraprendere?

- \[x] Ripristinare l'istanza dall'ultima immagine AMI. I controlli dello stato del sistema indicano che il filesystem dell'istanza è danneggiato.
- \[ ] Arrestare e avviare l'istanza. In questo modo l'istanza verrà spostata in un altro host.
- \[ ] Contatta il supporto AWS. Il mancato controllo dello stato del sistema indica un errore nell'hardware sottostante e deve essere risolto da un rappresentante AWS.
- \[ ] Riavviare l'istanza. Questo si fermerà e avvierà l'istanza e la sposterà in un altro host.

#### D25. Disponi di diversi server locali e desideri archiviare i tuoi backup offsite su AWS. Quale servizio di backup completamente gestito puoi utilizzare per spedire i tuoi backup ad AWS?

- \[ ] Windows Server 2016 supporta S3 come destinazione quando si utilizzano repliche di archiviazione.
- \[x] Utilizzare Storage Gateway.
- \[ ] Sincronizza i file direttamente su S3 con l'interfaccia a riga di comando di AWS.
- \[ ] Utilizzare la console RDS per forzare il riavvio dell'istanza del database in modo che il server primario diventi nuovamente il server master.

#### D26. Qual è la best practice per la creazione di un database PostgreSQL ad alta disponibilità in RDS in grado di sostenere la perdita di una singola regione AWS?

- \[ ] PostgreSQL non può essere replicato tra le regioni. Ripristinare i backup del database da un bucket S3 e reindirizzare le connessioni al database alla nuova istanza.
- \[ ] Crea repliche di lettura in altre regioni AWS. È possibile designare un nuovo database master da una qualsiasi delle repliche di lettura fino a quando l'errore regionale non viene risolto.
- \[ ] Verificare che l'istanza sia configurata per il supporto Multi-AZ. Le modifiche al database verranno sincronizzate automaticamente con un'altra area in caso di errore e RDS selezionerà automaticamente un nuovo master fino a quando l'errore regionale non verrà risolto.
- \[x] Crea repliche di lettura in altre regioni AWS. Verificare che le operazioni di lettura sul database vengano eseguite in una replica di lettura disponibile e inviare operazioni di scrittura a un'altra area se è necessario promuovere una replica di lettura a un database autonomo se il master è inattivo.

#### D27. È stata creata una nuova istanza Linux EC2 e installato PostgreSQL, ma non è possibile stabilire una connessione al server dal computer locale. Quali passaggi vengono eseguiti per risolvere il problema?

- \[ ] Creare una regola del gruppo di sicurezza che consenta tutto il traffico da 0.0.0.0/0. Questo verificherà se un'altra regola sta negando o meno il traffico.
- \[x] Verificare che i gruppi di sicurezza assegnati consentano il traffico dall'indirizzo IP alla porta 5432. Verificare che PostgreSQL sia configurato per l'ascolto del traffico esterno e sia associato all'interfaccia pubblica.
- \[ ] Assicurarsi di utilizzare un IP elastico e che sia incluso nel `postgresql.conf` file di configurazione.
- \[ ] Arrestare e avviare l'istanza. Le nuove regole del gruppo di sicurezza avranno effetto solo dopo un riavvio.

#### D28. A cosa serve il corpo informativo di questa politica del bucket S3?

```json
{
  "Sid": "bucketpolicy1",
  "Effect": "Allow",
  "Principal": "*",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::userreports/*",
  "Condition": {
    "IpAddress": { "aws:SourceIp": "68.249.108.0/24" },
    "NotIpAddress": { "aws:SourceIp": "68.249.108.128/32" }
  }
}
```

- \[ ] bucketpolicy1 consente a qualsiasi utente di eseguire qualsiasi azione sugli oggetti nel bucket userreports, ma limita gli oggetti alle autorizzazioni di sola lettura per chiunque provenga da 68.249.108.0 a 68.249.108.255, ad eccezione di 68.249.108.128.
- \[ ] bucketpolicy1 consente a qualsiasi utente proveniente dall'intervallo IP di 68.249.108.0 di accedere agli oggetti nel bucket userreports e nega l'accesso a 68.249.108.128.
- \[ ] bucketpolicy1 consente a qualsiasi utente di eseguire qualsiasi azione sugli oggetti nel bucket userreports, ad eccezione di chiunque provenga dall'IP di 68.249.108.128.
- \[x] bucketpolicy1 consente a qualsiasi utente proveniente dall'intervallo IP compreso tra 68.249.108.0 e 68.249.108.255 di accedere agli oggetti nel bucket userreports, ad eccezione di chiunque provenga dall'IP di 68.249.108.128.

#### D29. Un nuovo sviluppatore è stato aggiunto al team e ti è stato chiesto di fornire l'accesso all'account AWS dell'organizzazione. Qual è la procedura consigliata per concedere l'accesso?

- \[ ] Fornisci al nuovo sviluppatore l'accesso IAM assegnato al team di sviluppo. Questo utente IAM dovrebbe già includere tutte le policy di cui uno sviluppatore avrebbe bisogno.
- \[ ] Crea un utente IAM per il nuovo sviluppatore. Assegna manualmente le policy al nuovo account utente IAM.
- \[ ] Non concedere al nuovo sviluppatore l'accesso alla console AWS. Utilizzando l'utente IAM assegnato al gruppo di sviluppo, generare un nuovo set di chiavi di accesso ed etichettarle con il nome dello sviluppatore.
- \[x] Crea un utente IAM per il nuovo sviluppatore. Assegna al nuovo sviluppatore il gruppo di sviluppatori che hai già creato per gli altri sviluppatori.

#### D30. Quando si avvia un'istanza EC2 con un tipo di istanza che supporta l'archiviazione dell'istanza, quale caso d'uso è il migliore per lo storage dell'istanza?

- \[x] Utilizzare l'archiviazione dell'istanza per servire i file temporanei che richiedono una bassa latenza di I/O.
- \[ ] Utilizzare l'archiviazione dell'istanza per gestire i file caricati dagli utenti. Poiché è più sicuro di un volume EBS, è possibile isolare qualsiasi file dannoso dall'infezione del server.
- \[ ] Lo storage delle istanze è più veloce dei volumi EBS, quindi installa la radice del sistema operativo su questo volume per velocizzare le prestazioni del server.
- \[ ] L'archiviazione dell'istanza è un'opzione deprecata per l'archiviazione e non deve essere utilizzata.

#### D31. Qual è la procedura consigliata per ridimensionare orizzontalmente un'applicazione Web ASP.NET legacy che si basa su Active Directory ed è attualmente distribuita in una singola istanza windows EC2?

- \[x] Utilizzare Sysprep per arrestare l'istanza durante una finestra di manutenzione. Crea un'immagine AMI e posiziona entrambi i server dietro Application Load Balancer con sessioni permanenti.
- \[ ] Avviare un nuovo EC2 con la versione più recente di Windows Server e installare nuovamente l'applicazione. Utilizzare Application Load Balancer e sessioni permanenti per bilanciare tra i due server.
- \[ ] Creare un clone del server utilizzando un'immagine AMI e un Application Load Balancer dell'utente per bilanciare il traffico tra le due istanze utilizzando sessioni permanenti.
- \[ ] Il ridimensionamento orizzontale non è la migliore pratica in questa situazione. Aumenta le dimensioni dell'istanza EC2 esistente e ridimensiona verticalmente l'applicazione.

#### D32. A cosa serve questa piccola sezione di un modello CloudFormation?

```yaml
FlowLog:
  Type: AWS::EC2::FlowLog
  Properties:
    DeliverLogsPermissionArn: !GetAtt IamRole.Arn
    LogGroupName: FlowLogsGroup
    ResourceId: !Ref LogVpcId
    ResourceType: VPC
    TrafficType: ALL
```

- \[x] Scrive i log del flusso di rete VPC nel gruppo di log CloudWatch FlowLogsGroup. È possibile utilizzarlo per ispezionare le connessioni di rete del VPC.
- \[ ] Registra tutto il traffico di rete all'interno di un VPC ad eccezione degli ID istanza definiti da LogVpcID e lo registra nel gruppo di log CloudWatch FlowLogsGroup.
- \[ ] Registra tutto il traffico di rete da e verso una singola istanza EC2 nel gruppo di log di CloudWatch FlowLogsGroup. È possibile utilizzarlo per ispezionare il traffico di rete sospetto che entra in un'istanza EC2.
- \[ ] Registra tutte le richieste DNS effettuate dalle risorse all'interno di un VPC e le registra in CloudWatch FlowLogsGroup. Utilizzare questa opzione per diagnosticare gli errori di ricerca DNS all'interno dell'ambiente.

#### D33. Si eseguono contenitori Docker su ECS. Qual è la metrica più importante da monitorare?

- \[ ] Il conteggio dei container in esecuzione per ogni servizio da CloudWatch.
- \[ ] Lo stato dell'istanza di ogni istanza EC2 nel cluster da CloudWatch.
- \[ ] Monitorare la dashboard del servizio EC2. Guarda le interruzioni pubblicate al servizio ECS.
- \[x] Il consumo di memoria di ogni istanza EC2 nel cluster da CloudWatch.

#### D34. Application Load Balancer può instradare il traffico a diversi gruppi di destinazione in base a diverse condizioni. Quale di questi casi d'uso non è supportato da Application Load Balancer?

- \[ ] Una richiesta con un'intestazione HTTP X-Requested-With: la gestione temporanea può essere instradata a un gruppo di destinazione per un servizio ECS nell'ambiente di gestione temporanea.
- \[ ] Gli IP di origine corrispondenti a 192.0.2.0/24 su una porta listener di 1433 possono essere instradati a un gruppo di destinazione per un cluster RDS per SQL Server.
- \[ ] Un percorso di /signup\* può essere indirizzato a un gruppo di destinazione per una funzione Lambda che elabora le registrazioni di nuovi utenti.
- \[x] Una stringa di query HTTP POST di ? action=createuser può essere instradato a un gruppo di destinazione per un servizio ECS.

#### D35. Cosa fa un VPC?

- \[x] crea una rete basata su cloud per interconnettere un insieme di server e appliance virtuali
- \[ ] crea un tunnel sicuro tra due reti
- \[ ] crea un piano di archiviazione condiviso per la condivisione dei dati dell'applicazione tra più istanze.
- \[ ] crea una rete privata completamente isolata dalla rete Internet pubblica.

#### D36. Puoi perdere l'indirizzo IP pubblico associato alla tua istanza EC2?

- \[ ] Sì, puoi perderlo se riavvii l'istanza.
- \[x] Sì, puoi perderlo se arresti e avvii l'istanza.
- \[ ] No, non perderai mai l'indirizzo IP pubblico per la tua istanza.
- \[ ] Sì, puoi perderlo quando modifichi le proprietà dell'istanza e rilasci l'indirizzo IP.

#### D37. Qual è il posto migliore per archiviare i backup del database su un'istanza EC2 configurata come server di database?

- \[x] un bucket S3, sincronizzato con i backup del database tramite uno script che chiama l'interfaccia a riga di comando di AWS
- \[ ] Volume EBS collegato all'istanza
- \[ ] istanza associata all'istanza
- \[ ] instance storage, con uno script che replica i backup del database in un'altra istanza in una zona di disponibilità diversa.

#### D38. Quale di queste è una restrizione valida sulle proprietà di un VPC?

- \[ ] Puoi avere solo 10 gateway Internet per regione su un nuovo account AWS.
- \[ ] Puoi avere solo 10 VPC per regione su un nuovo account AWS
- \[x] Non è possibile creare un blocco CIDR con una netmask più grande di /16
- \[ ] Puoi avere solo 10 subnet all'interno di un VPC

#### D39. Hai un'istanza Linux EC2 che non risponde alle richieste e non puoi connetterti ad essa tramite SSH. Utilizzando la console EC2, hai emesso un comando per arrestare l'istanza, ma negli ultimi 10 minuti l'istanza è stata nello stato di "arresto". Qual è il prossimo passo che dovresti fare?

- \[x] Esegui un'altra azione di arresto tramite la console EC2 e scegli l'opzione per arrestare forzatamente l'istanza.
- \[ ] Creare un'immagine AMI dell'istanza e scegliere l'opzione per acquisire l'immagine senza riavviare l'istanza.
- \[ ] Modificate le proprietà dell'istanza e aumentate le dimensioni dell'istanza.
- \[ ] Contatta il supporto AWS. Qualsiasi ulteriore azione potrebbe danneggiare il file system.

#### D40. Si dispone di 14 server Web on-premise, 4 server di database, 6 server che utilizzano software GIS, 3 file server e 4 server di sviluppo. Quali considerazioni dovresti prendere in considerazione quando esegui la migrazione di questi server in AWS?

- \[ ] AWS non ha un modo per separare la fatturazione per i costi di elaborazione, quindi dovrai progettare un modo per dividere il budget tra i reparti.
- \[x] I nuovi account AWS sono limitati a 20 istanze EC2 on-demand. Invia una richiesta per aumentare i limiti tariffari prima di iniziare una migrazione.

#### D41. Man mano che l'applicazione Web cresce e le esigenze di monitoraggio delle applicazioni diventano più complesse, quale servizio di monitoraggio dei log aggiuntivo NON dovresti prendere in considerazione?

- \[ ] Stack ELK: Elasticsearch, Loggly e Kibana
- \[x] PRTG
- \[ ] Nuova Reliquia
- \[ ] Datadog

#### D42. Hai un'istanza EC2 T2 fondamentale per la tua infrastruttura. Come monitoreresti la metrica più importante per questa istanza?

- \[x] Attiva CloudWatch Auto Recovery e posiziona i monitor sui controlli Stato del sistema e Stato istanza affinché l'istanza ti avvisi quando uno dei due è in allarme.
- \[ ] Usa CloudWatch per mettere i monitor sui crediti CPU rimanenti. Se si esaurisce il credito della CPU, l'istanza verrà arrestata.

#### D43. Quale funzione può essere utilizzata per rispondere a un improvviso aumento del traffico web?

- \[ ] Gruppi EC2 Auto Scaling
- \[ ] AWS Shield Advanced
- \[ ] Repliche di lettura RDS
- \[x] tutte queste risposte

#### D44. Se un set di server si trova all'interno di una subnet privata del tuo VPC, come puoi connettere tali server ai server locali?

- \[ ] Stabilisci una connessione con AWS Direct Connect.
- \[ ] Utilizza AWS Client VPN.
- \[ ] Installare un server OpenVPN su un'istanza che si trova all'interno della subnet con un IP elastico.
- \[x] Tutte queste opzioni possono stabilire una connessione a una subnet privata.

#### D45. Si dispone di un servizio di bilanciamento del carico UDP creato da un'istanza che esegue un proxy NGINX. La soluzione APM (Application Performance Management) è in grado di rilevare errori nell'istanza del servizio di bilanciamento del carico e trasferire Elastic IP a un'istanza di standby passivo. Utilizzando l'interfaccia a riga di comando di AWS, quale script programmi nel tuo APM per spostare l'IP elastico?

- \[x] A

<!---->

    aws ec2 disassociate-address --association-id eipassoc-2bebb712
    aws ec2 associate-address --instance-id i-8b953 --allocation-id eipalloc-02d021a

- \[ ] B

<!---->

    aws ec2 release-address --association-id eipassoc-2bebb712
    aws ec2 assign-address --instance-id i-8b953 --allocation-id eipalloc-02d021a

- \[ ] C

<!---->

    aws ec2 stop-instances --instance-ids i-8b953
    wait 30
    aws ec2 disassociate-address --association-id eipassoc-2bebb712
    aws ec2 associate-address --instance-id i-8b953 --allocation-id eipalloc-02d021a
    aws ec2 start-instances --instance-ids i-8b953

- \[ ] D

<!---->

    aws ec2 release-address --association-id eipassoc-2bebb712
    aws ec2 associate-address --instance-id i-8b953 --allocation-id eipalloc-02d021a

#### D46. Quale servizio può ospitare i contenitori Docker?

- \[ ] Lightsail
- \[ ] Elastic Container Service (ECS)
- \[ ] Elastic Compute Cloud (EC2)
- \[x] Tutti questi servizi possono ospitare un contenitore Docker.

#### D47. Nella console S3, sotto la colonna Access, cosa indica il badge pubblico accanto al nome del bucket?

![image](images/002.png?raw=png)

- \[x] A tutti gli oggetti all'interno di questo bucket viene assegnato l'accesso pubblico e potrebbero essere leggibili o scrivibili da chiunque su Internet. Assicurati che nessun dato sensibile venga condiviso pubblicamente all'interno di questo bucket.
- \[ ] Tutti gli oggetti all'interno di questo bucket sono scrivibili, il che significa che Internet pubblico ha la possibilità di caricare qualsiasi file direttamente sul bucket S3. Il bucket S3 potrebbe essere utilizzato per servire malware.
- \[ ] Ad alcuni oggetti all'interno di questo bucket viene assegnato l'accesso pubblico. Verificare che tutti gli oggetti condivisi pubblicamente all'interno di questo bucket non contengano dati sensibili.
- \[ ] Gli oggetti all'interno di questo bucket possono essere resi pubblici, se l'ACL su tale oggetto è impostato per consentire l'accesso a tutti. I bucket privati non consentono di impostare autorizzazioni pubbliche su alcun oggetto.

#### D48. Quali privilegi sono specifici dell'account root AWS e non possono essere concessi a un altro utente IAM sull'account?

- \[ ] Revoca il ruolo AdministratorAccess o concedilo a un altro utente IAM.
- \[ ] Creare una nuova hosted zone in Route 53.
- \[x] Elimina l'account AWS.
- \[ ] Modificare i dettagli di fatturazione.

#### D49. La tua domanda invia 50.000 e-mail tramite SES ogni giorno. Dal momento che è necessario mantenere una bassa frequenza di rimbalzo per evitare di essere messi in libertà vigilata, quale semplice sistema si progetta per elaborare automaticamente i rimbalzi duri?

- \[x] Configurare SES per inviare tutti gli eventi di rimbalzo a un argomento SNS. Creare una funzione Lambda che elabori ogni evento di hard bounce e contrassegni automaticamente tale account come rimbalzo nell'applicazione per impedire ulteriori tentativi di invio.
- \[ ] Configura SES in modo che non invii più agli indirizzi e-mail presenti nell'elenco di rimbalzo.
- \[ ] Configurare SES per inviare i registri di tutti i tentativi di consegna tramite Kinesis Firehose. Elabora ogni evento e cerca i tipi di rimbalzo e rimuovi queste e-mail dal tuo elenco.
- \[ ] Invia tutte le e-mail tramite SES con un'intestazione di risposta personalizzata. Configura SES per ascoltare gli eventi su questo indirizzo e-mail e contrassegna qualsiasi indirizzo e-mail che risponde a questo account come messaggio respinto e rimuovilo dalla tua mailing list.

#### D50. La tua applicazione web sta ricevendo una quantità sospetta di richieste errate da indirizzi IP stranieri. La tua attività opera solo in pochi paesi e vorresti bloccare qualsiasi altro traffico. Qual è la best practice per limitare l'accesso all'applicazione Web in base al paese?

- \[x] Utilizzare Web Application Firewall e creare una condizione di corrispondenza geografica per eliminare tutte le richieste provenienti da paesi che non sono presenti nell'elenco dei dispositivi consentiti.
- \[ ] Utilizzare Application Load Balancer per creare una nuova regola di routing che esamina l'indirizzo IP di origine. Aggiungi un blocco IP per i paesi che hanno accesso.
- \[ ] Ospita il front-end del tuo sito Web in CloudFront e configura una restrizione geografica sulla distribuzione.
- \[ ] Utilizzare CloudTrail per monitorare gli indirizzi IP delle richieste errate. Utilizzare Lambda per aggiungere questi indirizzi IP a una regola di Application Load Balancer che blocca gli IP.

#### D51. Qual è la procedura consigliata per la gestione delle istanze Windows EC2 e l'applicazione degli aggiornamenti?

- \[ ] Attiva l'aggiornamento automatico in Windows Update su ogni EC2 avviato oppure crea la tua AMI con questa funzione abilitata e avvia tutte le tue istanze EC2 da questa AMI.
- \[ ] Creare un programma di manutenzione che un dipendente deve compilare ogni settimana confermando che è stata condotta un'ispezione visiva di ogni istanza e quali patch sono state applicate.
- \[x] Utilizza AWS Systems Manager Patch Manager per trovare le istanze di patch che richiedono aggiornamenti durante una finestra di manutenzione impostata.
- \[ ] Installare Windows Server Update Services nel controller Active Directory primario.

#### D52. Oltre a CloudFormation, puoi utilizzare altri strumenti di orchestrazione per automatizzare la formazione e la manutenzione dei server. Quale strumento è _non_ una scelta efficiente per l'orchestrazione di una grande infrastruttura?

- \[ ] Chef
- \[ ] Ansible
- \[ ] Burattino
- \[x] Vagabondo

#### D53. Cosa succede a un'istanza rdS di SQL Server se i database aumentano di dimensioni e superano lo spazio allocato?

- \[ ] RDS aumenterà automaticamente lo spazio allocato del 10% e invierà all'account root AWS un'e-mail con i passaggi di risoluzione. Assegna più spazio per evitare addebiti eccessivi.
- \[x] L'istanza del database segnalerà uno stato STORAGE_FULL e diventerà inaccessibile se l'istanza non dispone di spazio di archiviazione rimanente sufficiente per funzionare. Allocare più spazio all'istanza.
- \[ ] SQL Server chiuderà tutte le connessioni esistenti ai database e tenterà di ridurre i file di log per recuperare spazio di archiviazione.
- \[ ] RDS aumenterà automaticamente lo spazio assegnato del 5% e continuerà ad allocare nuovo spazio fino al 50% dello spazio allocato originariamente. Quando lo spazio di archiviazione è aumentato del 50%, RDS arresterà automaticamente l'istanza per preservare l'integrità dei dati.

#### D54. Si dispone di una flotta di dispositivi IoT che inviano dati di telemetria a un'applicazione lato server fornita dal fornitore IoT per la decodifica di un formato di messaggistica proprietario. I dispositivi vengono sottoposti a provisioning per inviare report di telemetria al server tramite UDP sulla porta 6339. Qual è il modo migliore per scalare questo server man mano che vengono aggiunti più dispositivi IoT alla tua flotta?

- \[ ] Utilizzare un Network Load Balancer per distribuire il traffico tra i server. Utilizzare i controlli di integrità UDP per determinare se il server è disponibile per ricevere traffico.
- \[x] Utilizzare Route 53 con i controlli di integrità HTTP. Creare un'applicazione sul server per segnalare lo stato di preparazione del software server fornito dal fornitore a Route 53 tramite HTTP.
- \[ ] Utilizzare Route 53 con i controlli di integrità UDP. Man mano che si aumenta la scalabilità verticale, Route 53 instrada il traffico verso i nuovi server se superano i controlli di integrità.
- \[ ] Utilizzare Application Load Balancer per distribuire il traffico tra i server.

#### D55. le regole in uscita di un gruppo di sicurezza consentono solo il traffico che va a 0.0.0.0/0 sulla porta TCP 22 (SSH) e sulla porta TCP 3306 (MySQL). Esamina le regole in ingresso elencate nell'immagine seguente. Qual è il problema più importante da risolvere con questa configurazione del gruppo di sicurezza, per un'istanza EC2 di Ubuntu che funge da server Web?

![image](https://user-images.githubusercontent.com/8637045/112515574-c077e780-8d6c-11eb-96a6-11f27a0547cf.png?raw=png)

- \[ ] Le regole in uscita bloccano la porta UDP 53, quindi il server non sarà in grado di risolvere alcuna ricerca DNS.
- \[x] Le regole in uscita non consentono al traffico HTTP di lasciare l'istanza, pertanto le richieste HTTP in ingresso avranno esito negativo perché i client non riceveranno mai risposte HTTP.
- \[ ] La porta SSH in entrata non deve essere aperta al pubblico. Limita SSH a un singolo indirizzo IP o intervallo IP di indirizzi controllati oppure utilizza una VPN per accedere al VPC per questo server.
- \[ ] Tutte le porte TCP in ingresso sono esposte, il che sostituisce le regole HTTP e SSH ed espone tutte le porte TCP alla rete Internet pubblica.

#### D56. Un'istanza EC2 che esegue un sito WordPress continua a essere violata, anche se hai ripristinato il server più volte e hai patchato WordPress. Quale servizio AWS può aiutarti a rilevare e prevenire ulteriori attacchi?

- \[ ] CloudWatch
- \[x] GuardDuty
- \[ ] Scudo
- \[ ] Consulente per la sicurezza

#### D57. Un client non tecnico desidera migrare un sito WordPress in AWS da un server privato gestito da una società di hosting di terze parti. A quale servizio AWS consigliare di eseguire la migrazione del sito?

- \[ ] CloudFront
- \[ ] Un'istanza EC2 lanciata dall'AMI WordPress ufficiale
- \[ ] S3
- \[x] Lightsail

#### D58. La tua azienda dispone di server on-premise con una soluzione di backup in loco esistente che replica anche i backup in un altro campus dall'altra parte del paese con la propria soluzione di backup in loco. Ti è stato chiesto di creare un terzo livello di ridondanza archiviando anche questi backup nel cloud. In caso di guasto di un backup primario e secondario, il tuo capo vuole sapere che i backup cloud possono essere accessibili il più velocemente possibile per ridurre i tempi di inattività durante il ripristino. Quale classe di storage S3 consigliate per costi e prestazioni?

- \[ ] S3 Standard
- \[ ] S3 Intelligent-Tiering
- \[ ] Ghiacciaio S3
- \[x] S3 Accesso infrequente a una zona

#### D59. Quale archivio di Big Data ti consentirà di archiviare grandi flussi di dati sull'attività degli utenti provenienti da applicazioni web e mobili?

- \[ ] Nettuno
- \[ ] Aurora
- \[ ] RDS per SQL Server
- \[x] Redshift

#### D60. Qual è l'opzione migliore per Auto Scaling delle istanze EC2 per modelli di traffico prevedibili?

- \[x] scala in base a una pianificazione
- \[ ] ridimensionamento manuale
- \[ ] scala in base alla domanda
- \[ ] mantenere i livelli attuali in ogni momento

#### D61. Stai migrando un cluster RabbitMQ on-premise in AWS. Quale percorso di migrazione scegliere per facilitare sia la manutenzione che la distribuzione?

- \[ ] Riscrivere le parti dell'applicazione che utilizzano RabbitMQ per utilizzare SQS.
- \[ ] Avvia un cluster RabbitMQ con istanze EC2 utilizzando un'AMI supportata.
- \[ ] Riscrivere le parti dell'applicazione che utilizzano RabbitMQ per utilizzare Kinesis.
- \[x] Riscrivi le parti della tua applicazione che utilizzano RabbitMQ per utilizzare Amazon MQ.

#### D62. Quando si crea una nuova istanza RDS, a cosa serve l'opzione Multi-AZ?

- \[ ] replica i backup del database su S3 e li rende disponibili in tutte le regioni per prevenire qualsiasi perdita di dati
- \[x] crea una seconda istanza di database passiva all'interno della stessa area che diventerà il database primario durante un failover
- \[ ] crea un cluster di database a disponibilità elevata che ospiterà il cluster di database in almeno due aree
- \[ ] crea un'altra istanza di database in un'altra area e mantiene attivo un hot standby per il failover durante gli errori regionali

#### D63. Qual è la migliore classe di istanza EC2 per un server che ha continuamente un carico di CPU elevato?

- \[x] C5
- \[ ] T2
- \[ ] R5
- \[ ] H1

#### D64. Il sistema di gestione delle prestazioni delle applicazioni (APM) è in grado di leggere lo stato dei monitor CloudWatch ed eseguire azioni tramite script. Quando il parametro StatusCheckFailed di CloudWatch entra in uno stato non riuscito (valore 1), si desidera che l'APM ripristini automaticamente l'istanza. Quale script usi?

- \[x] A

<!---->

    aws ec2 stop-instances --instance-ids i-0b263919b6498b123
    aws ec2 start-instances --instance-ids i-0b263919b6498b123

- \[ ] B

<!---->

    aws ec2 reboot-instances --instance-ids i-0b263919b6498b123

- \[ ] C

<!---->

    aws ec2 reboot-instances --instance-ids i-0b263919b6498b123
    wait 30
    aws ec2 start-instance --instance-ids i-0b263919b6498b123

- \[ ] D

<!---->

    aws ec2 reboot-instances --instance-ids i-0b263919b6498b123
    aws ec2 start-instances --instance-ids i-0b263919b6498b123

#### D65. Cosa c'è di sbagliato nella terza regola del gruppo di sicurezza in entrata, che consente a tutto il traffico da sg-269afc5e di andare a un'istanza EC2 di Ubuntu configurata come server web?

![065](https://user-images.githubusercontent.com/33999631/179728393-8a2636ea-04e7-4597-b0cc-8150e2bc91de.png?raw=png)

- \[ ] Tutto il traffico su tutte le porte viene negato in questa istanza, che sovrascrive la regola HTTP e la rende ridondante.
- \[x] L'istanza è stata avviata con il gruppo di sicurezza predefinito, ma non è possibile per un amministratore accedere a SSH nell'istanza.
  Aggiungere un'altra regola che consenta l'accesso SSH da un'origine protetta, ad esempio un singolo IP o un intervallo di indirizzi IP gestiti.
- \[ ] Non c'è niente di sbagliato in questa regola del gruppo di sicurezza. Supponendo che sg-269afc5e sia applicato ad altre risorse che sono correttamente
  protetto, questa regola consente a tutto il traffico di passare attraverso il quale è anche assegnato il gruppo di sicurezza sg-269afc5e.
- \[ ] Tutto il traffico su tutte le porte è consentito in questa istanza. In questo modo l'istanza viene esposta a tutto il traffico Internet pubblico e
  sovrascrive la regola HTTP in ingresso.

#### D66. Hai un VPC che ha una sottorete pubblica e privata. Nella subnet pubblica è presente un gateway NAT che consente alle istanze della sottorete privata di accedere a Internet senza avere un'esposizione pubblica al di fuori del VPC. Quali devono essere le tabelle di routing per la subnet privata?

![image](images/003.png?raw=png)

- \[x] A

<!---->

    Destination 1: 10.0.0.0/16, Target 1: local;
    Destination 2: 0.0.0.0/0, Target 2: nat-09b4832

- \[ ] B

<!---->

    Destination 1: 10.0.0.0/24, Target 1: local;
    Destination 2: 0.0.0.0/0, Target 2: igw-b2ff47d6

- \[ ] C

<!---->

    Destination 1: 10.0.0.0/24, Target 1: subnet-1948ba2;
    Destination 2: 0.0.0.0/0, Target 2: nat-09b4832

- \[ ] D

<!---->

    Destination 1: 10.0.0.0/16, Target 1: vpc-12bd09ac2;
    Destination 2: 0.0.0.0/0, Target 2: igw-b2ff47d6

#### D67. Per soddisfare i requisiti di auditing di alcuni standard di conformità, quale strumento AWS può essere abilitato per mantenere un log di controllo dell'accesso e delle modifiche all'infrastruttura AWS?

- \[x] CloudTrail
- \[ ] CloudWatch
- \[ ] Strumento di audit e conformità AWS
- \[ ] GuardDuty

#### D68. Si dispone di un'applicazione che genera report a esecuzione prolungata, li archivia in un bucket S3 e quindi invia un'e-mail all'utente che ha richiesto il report con un collegamento per scaricarlo. Qual è la procedura consigliata per l'archiviazione dei dati del report in S3?

- \[ ] Creare un bucket S3 pubblico. Quando l'applicazione crea l'oggetto report in S3, generare due lunghi generati in modo casuale
  nomi di cartelle e posizionare il file all'interno della sottocartella più profonda. Impostare il criterio di conservazione sull'oggetto su un'ora e inviare questo collegamento tramite posta elettronica a
  l'utente. Il link sarà attivo per un'ora.
- \[ ] Creare un bucket S3 pubblico. Utilizzare un hash dell'indirizzo e-mail dell'utente e la data e l'ora in cui è stato richiesto il report per generare un
  nome oggetto univoco. Inviare questo collegamento tramite posta elettronica all'utente e fare in modo che un'attività pianificata venga eseguita all'interno dell'applicazione per rimuovere gli oggetti meno recenti
  di sette giorni.
- \[x] Creare un bucket S3 privato. Il collegamento nell'e-mail dovrebbe portare l'utente all'applicazione, dove è possibile verificare l'utente attivo
  o forzare l'utente ad accedere. Dopo aver verificato che l'utente disponga dei diritti di accesso a questo file, chiedere all'applicazione di recuperare l'oggetto
  da S3 e restituirlo nella risposta HTTP. Eliminare il file dal bucket S3 al termine della richiesta.
- \[ ] Creare un bucket S3 privato. Il collegamento nell'e-mail dovrebbe portare l'utente all'applicazione, dove è possibile verificare l'utente attivo
  o forzare l'utente ad accedere. Impostare l'oggetto report in S3 su public. Mostra all'utente un pulsante "Download" nel browser che collega
  all'oggetto pubblico.

#### D69. Quando si invia un grande volume di e-mail tramite SES, qual è l'insieme più importante di metriche da monitorare?

- \[x] il tuo reclamo e le frequenze di rimbalzo
- \[ ] si apre e fa clic
- \[ ] clic e consegne
- \[ ] invio del volume negli ultimi 15 minuti e nell'arco di un giorno per tenere d'occhio i picchi di fatturazione

#### D70. Stai per ospitare un'applicazione che utilizza un database MySQL. Quale database selezionare se non si desidera gestire le attività di ridimensionamento o di amministrazione del database?

- \[ ] Avviare un'immagine AMI dal marketplace contenente un server MySQL preconfigurato.
- \[x] Aurora
- \[ ] RDS per MySQL
- \[ ] Redshift

#### D71. Un modulo nell'applicazione Web invia i dati di iscrizione a "http://example.com/signup/new?source=web" e questi dati devono essere gestiti da un servizio ECS dietro Application Load Balancer (ALB). Quale regola ALB indirizzerà questa richiesta?

![image](images/004.png?raw=png)

- \[ ] A

<!---->

    IF (all match)
        Path is /signup*
        Query string is signup:new
    Then
        Forward to ecs-cluse-service <there is a typo - yes!

- \[ ] B

<!---->

    IF (all match)
        Path is /sign/new/&
        Query request method is POST
    Then
        Forward to ecs-cluse-service

- \[ ] C ... Un altro con POST
- \[x] D ... Solo uno con Get

#### D72. Quale servizio AWS può ospitare il server delle applicazioni Web per un sito WordPress?

- \[ ] S3
- \[x] Gambo elastico dei fagioli
- \[ ] ElasticCache
- \[ ] CloudFront

#### D73. Cosa fa la seguente interfaccia a riga di comando AWS `create-service` comando per ECS fare?

    aws ecs create-service \
     --cluster production \
     --service-name rest-api \
     --task-definition rest-api:1 \
     --desired-count 2 \
     --launch-type "FARGATE" \
     --network-configuration \
     "awsvpcConfiguration={subnets=[subnet-0b29129ab],securityGroups=[sg-0b29129ab]}"

- \[ ] modifica i gruppi di sicurezza del running **rest-api** compito
- \[ ] crea un cluster chiamato **produzione** e lancia due container in Fargate con il **rest-api** definizione delle attività
- \[x] lancia due container su Fargate nell'esistente **produzione** utilizzando il cluster **rest-api** definizione delle attività
- \[ ] crea una definizione di servizio per il **rest-api** compito; inserire due contenitori nel cluster di produzione all'avvio **ecs-cli** su, comando

#### D74. Vuoi rendere la tua API pubblica rapidamente accessibile da tutte le regioni. Qual è il modo migliore per farlo?

- \[ ] Creare un singolo endpoint gateway API in un'area centrale.
- \[ ] Creare un endpoint gateway API privato per ogni regione.
- \[ ] Creare un endpoint gateway API regionale per ogni area.
- \[x] Crea endpoint gateway API ottimizzati per i bordi e distribuiscili in una rete CloudFront.

#### D75. Che tipo di soluzione di dati è consigliabile utilizzare per i dati provenienti da dati non relazionali e relazionali provenienti da dispositivi IoT, siti Web, app mobili, ecc.?

- \[ ] Amazon DynamoDB
- \[x] Formazione di AWS Lake
- \[ ] Amazon Redshift
- \[ ] Amazon Aurora

#### D76. Si dispone di una suite di analisi che produce report sui modelli di utilizzo dell'applicazione Web. Dopo aver completato la migrazione ad AWS e aver utilizzato Application Load Balancer per bilanciare il carico nell'applicazione Web, il reparto marketing ha notato che i report basati sulla posizione sul traffico Web mostrano solo il traffico proveniente da una singola posizione. Qual è il problema?

- \[ ] Utilizzare un servizio di bilanciamento del carico classico, non Application Load Balancer.
- \[x] Application Load Balancer non conserva l'indirizzo IP di origine originale. Il software di analisi deve essere configurato per esaminare l'intestazione della richiesta HTTP "X-Forwarded-For" per l'indirizzo IP di origine corretto.
- \[ ] Application Load Balencer deve essere configurato per mantenere l'indirizzo IP di origine del traffico che sta inoltrando. Crea una policy che abiliti il supporto proxyProtocol e collegala all'ALB utilizzando l'interfaccia a riga di comando di AWS.
- \[ ] Configurare le istanze EC2 del server Web in modo che dispongano solo di indirizzi IP privati. Gli indirizzi IP pubblici delle istanze vengono registrati nei registri del server Web, solo ALB bug dovrebbe avere un'interfaccia pubblica e indirizzerà il traffico alle istanze tramite l'interfaccia privata.

#### D77. Cos'è `not` un utente predefinito di un'istanza Linux comune avviata da un'AMI?

- \[ ] ubuntu
- \[x] sistema-utente
- \[ ] ec2-utente
- \[ ] admin

[Riferimento](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connection-prereqs.html)

#### D78. Hai replicato l'infrastruttura che serve l'API back-end per la tua applicazione Web in tutte le regioni per servire meglio i tuoi clienti negli Stati Uniti e nell'UE. Qual è il modo migliore per indirizzare la tua applicazione web al data center più vicino?

- \[x] Utilizza la Route 53 con ricerche di geolocalizzazione per indirizzare il traffico tra le due regioni.
- \[ ] Creare una regola di reindirizzamento WAF che reindirizza il traffico al data center dell'UE se l'IP di origine proviene da determinati paesi.
- \[ ] Acquista un'estensione di dominio nazionale e indirizza i tuoi utenti al sito corretto, ad esempio example.com e example.co
- \[ ] Chiedi all'applicazione front-end di testare la latenza tra ogni data center e di utilizzare il data center che risponde più velocemente.

[Riferimento](https://aws.amazon.com/premiumsupport/knowledge-center/geolocation-routing-policy/)

#### D79. Hai recentemente lanciato il tuo nuovo prodotto web e ti aspetti 1.000 nuovi utenti ogni mese. Tuttavia, hai appena ricevuto la notizia dal CEO che il tuo prodotto sarà presentato in una prossima conferenza coperta da diversi media, e questo potrebbe portare a 20.000 nuovi utenti nel corso della prossima settimana. Come si pianifica un improvviso aumento del traffico?

- \[ ] Replica la tua infrastruttura in due regioni. L'applicazione verrà rafforzata a un errore regionale e raddoppierà la capacità.
- \[ ] Acquisire un'immagine AMI di un server front-end per salvare la configurazione e quindi aggiungere altri server al cluster pror alla conferenza. Rimuovere i server dal cluster dopo il picco dalla conferenza.
- \[ ] Test per determinare la velocità effettiva e il numero di utenti che è possibile supportare. Sviluppa un piano di scalabilità per front-end, microservizi e database basato su parametri CloudWatch in linea con i colli di bottiglia testati.
- \[x] Utilizza i gruppi Auto Scaling per creare più server front-end quando i parametri di CloudWatch per l'utilizzo della CPU su una singola istanza superano l'80% per cinque minuti.

[Riferimento](https://aws.amazon.com/ec2/autoscaling/)

#### D80. Come ci si connette tramite SSH a un'istanza Linux EC2 con un volume EBS se si perde la coppia di chiavi?

- \[ ] Arrestare l'istanza e creare un'immagine AMI. Avviare l'immagine utilizzando una nuova coppia di chiavi.
- \[ ] Contatta il supporto AWS. Uno specialista del supporto può ripristinare in remoto l'accesso all'istanza e inviarti una nuova coppia di chiavi.
- \[ ] Non è possibile connettersi a questa istanza EC2. La coppia di chiavi viene visualizzata una sola volta. Se lo perdi, hai perso tutto l'accesso a questa istanza. Collegare il volume EBS a un'altra istanza per ripristinare i file.
- \[x] Collegare il volume EBS a un'istanza temporanea avviata con una nuova coppia di chiavi e sovrascrivere ~/.ssh/authorized_keys utilizzando lo stesso file della nuova istanza.

[Riferimento](https://medium.com/the-10x-dev/how-to-recover-access-login-to-your-aws-instance-after-losing-your-pem-keypair-file-e0d31bae2da4)

#### D81. Il data center on-premise (172.16.128.0/24) è già connesso al VPC AWS (10.0.0.0/16) tramite un gateway cliente. Desideri collegare un altro data center per un'azienda che hai appena acquisito (172.16.130.0/24) al tuo VPC come mostrato nell'immagine. Qual è il modo migliore per creare questo link?

![image](images/Q80.png?raw=png)

- \[ ] Stabilire una connessione tra i due data center e collegare il secondo data center al primo attraverso un tunnel privato. Il traffico fluirà dal secondo data center e poi attraverso i primi dati e poi in AWS.
- \[ ] Creare un secondo gateway cliente e configurare il client VPN nel secondo data center per la connessione al gateway privato virtuale.
- \[x] Creare un secondo gateway privato virtuale (VPG) e collegarlo al VPC. Crea un gateway cliente per il nuovo gateway privato virtuale e utilizza il tuo client VPN nel tuo secondo data center per stabilire una connessione al VPG.
- \[ ] Non è possibile avere più di un gateway cliente per VPC, quindi la soluzione proposta non funzionerà. Crea un secondo VPC con un gateway privato virtuale e un gateway cliente. Collega i due VPC utilizzando il peering VPC.

#### D82. Si sta eseguendo la migrazione di un database da 200 GB da un SQL Server locale a RDS per SQL Server. Il database deve avere tempi di inattività minimi durante la migrazione. Qual è la procedura consigliata per la migrazione di questo database?

- \[ ] Chiudere tutte le connessioni esistenti al database di SQL Server e utilizzare Il servizio Migrazione database per trasferire i dati a Servizi Desktop remoto.
- \[x] Utilizzare Il servizio migrazione database per replicare il database in Servizi Desktop remoto e mantenerlo sincronizzato durante la migrazione. Eseguire nuovamente il repoint delle applicazioni per l'utilizzo del nuovo endpoint RDS.
- \[ ] Scollegare il database di SQL Server durante la migrazione. Esegui un backup del database e utilizza SQ con Accelerated Transfer per caricare i backup su S3. Ripristinare i backup nell'istanza RDS.
- \[ ] Utilizzare l'Importazione/Esportazione guidata in SQL Server Enterprise Manager per creare un'attività di esportazione ed esportare le tabelle nell'istanza RDS.

[Riferimento](https://aws.amazon.com/dms/)

#### D83. Hai abilitato l'autenticazione a più fattori (MFA) per il tuo account root AWS e hai perso il tuo dispositivo MFA. Cosa devi fare per recuperare l'accesso al tuo account?

- \[ ] Non è possibile ripristinare l'accesso al tuo account root AWS. Contatta il supporto AWS.
- \[x] Verrà inviata un'e-mail all'indirizzo e-mail in archivio per verificare la proprietà dell'account. Dovrai quindi fornire il numero di telefono sull'account.
- \[ ] Verrà inviata un'e-mail all'indirizzo e-mail registrato. Dopo aver fatto clic sul collegamento nell'e-mail, fornire uno dei codici di recupero MFA creati quando MFA è stato abilitato.
- \[ ] Utilizza l'interfaccia a riga di comando di AWS con il token di accesso all'account root per disabilitare MFA sull'account root. Quindi utilizzare l'interfaccia della riga di comando per impostare una nuova password sull'account root.

[Riferimento](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_lost-or-broken.html)

#### D84. Come si assegna un IP elastico a più istanze EC2?

- \[ ] Nella dashboard VPC, fai clic su IP elastici. Selezionare l'IP elastico e fare clic su Associa indirizzo. Seleziona ogni istanza EC2 a cui desideri assegnare questo indirizzo.
- \[ ] Nella dashboard di EC2, fare clic su Istanza EC2. In Azioni selezionare Rete > Gestisci indirizzi IP. fare clic per aggiungere un nuovo indirizzo IP e digitare l'indirizzo dell'IP elastico. Ripeti il processo per ogni istanza EC2 a cui desideri assegnare questo IP elastico.
- \[ ] Utilizza l'interfaccia a riga di comando di AWS e passa diverse opzioni '--instance-id' al comando aws ec2 assosiate-address.
- \[x] Non è possibile assegnare un IP elastico a più istanze EC2. Può essere associato solo a una singola istanza EC2.

[Riferimento](https://stackoverflow.com/questions/54742522/assign-multiple-ec2-instances-to-one-elastic-ip)

#### D85. Hai creato un VPC con una subnet pubblica e una sottorete privata. Un server Web è stato inserito nella subnet pubblica e un server di database è stato inserito nella subnet privata. Il server Web è in grado di connettersi al server di database; tuttavia, il server di database in 10.0.1.2 non è in grado di ottenere gli aggiornamenti software. Qual è la causa di questo problema?

- \[x] Non esiste un gateway NAT per la subnet privata, quindi il server di database non dispone di route che gli consentano l'accesso pubblico a Internet per scaricare gli aggiornamenti software.
- \[ ] Al server di database deve essere assegnato un indirizzo pubblico dal pool o un IP elastico simile all'istanza 10.0.0.2.
- \[ ] Il router non è configurato correttamente sul VPC. Aggiungi una route alla tabella di routing per il VPC che instrada tutto il traffico per 0.0.0.0/0 all'ID del gateway Internet.
- \[ ] Non esiste un gateway Internet di sola uscita collegato alla sottorete privata del VPC.

#### D86. Vantaggio dell'utilizzo di S3 Glacier?

- \[ ] tempo di accesso
- \[ ] conservare per piccola durata
- \[x] costo
- \[ ] cross-region
