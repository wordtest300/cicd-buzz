# Microsoft Cloud Adoption Framework (CAF)

** Studentnummer: 1847568 | Uniserver System Administrator**
**Cloud Governance — TICT-CDU4GOV-24 | Hogeschool Utrecht | 2025–2026**

---

## Wat is het Microsoft Cloud Adoption Framework?

Het Microsoft Cloud Adoption Framework (CAF) voor Azure is een open-source verzameling van best practices, richtlijnen en tools die organisaties helpen bij het succesvol adopteren van cloudtechnologie. Het is door Microsoft ontwikkeld op basis van ervaringen bij duizenden klantimplementaties wereldwijd en is gratis beschikbaar via [docs.microsoft.com](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/).

CAF beschrijft zes samenhangende fasen:

| Fase | Doel |
|------|------|
| **Strategy** | Waarom naar de cloud? Welke business drivers? |
| **Plan** | Wat migreren we wanneer? Roadmap opstellen. |
| **Ready** | Landing zone inrichten — veilige cloud-omgeving klaarzetten. |
| **Adopt** | Migratie uitvoeren of nieuwe applicaties bouwen. |
| **Govern** | Governance-discipline opbouwen en handhaven. |
| **Manage** | Day-2 operations — beheer, monitoring, optimalisatie. |

De **Govern**-fase is direct relevant voor het vak Cloud Governance.

---

## Hoe draagt CAF bij aan Cloud Governance?

De Govern-fase van CAF definieert vijf governance-disciplines die samen een compleet raamwerk vormen:

### 1. Cost Management
Beleid voor kostenbeheersing, budgetten en FinOps-processen. Voorbeelden: verplichte resource-tags, budget alerts, maandelijkse rightsizing-reviews.

### 2. Security Baseline
Minimale beveiligingsnormen voor alle cloudresources. CAF verwijst naar de Azure Security Benchmark als startpunt. Voorbeelden: verplichte encryptie, MFA voor alle gebruikers, NSG-regels als code.

### 3. Resource Consistency
Standaardisatie van naming conventions, tagging, resource group structuur en deploymentprocedures. Dit zorgt voor voorspelbaarheid en vermindert operationele fouten.

### 4. Identity Baseline
Beheer van identiteiten en toegangsrechten. CAF adviseert Azure AD met Privileged Identity Management (PIM) voor just-in-time toegang en Conditional Access voor risicogebaseerde authenticatie.

### 5. Deployment Acceleration
Gestandaardiseerde en geautomatiseerde deploymentprocessen via Infrastructure as Code (Bicep of Terraform). Dit maakt omgevingen reproduceerbaar en auditeerbaar.

---

## CAF in de context van Uniserver

Als System Administrator bij Uniserver werk ik op een sovereign private cloud platform. CAF is primair voor Azure ontworpen, maar de governance-principes zijn ook toepasbaar op private cloud:

- **Resource Consistency** → Uniserver gebruikt standaard VM-templates en Ansible playbooks voor consistente uitrol van klantenomgevingen
- **Identity Baseline** → Uniserver hanteert RBAC per klantenomgeving met strikte toegangslogging voor de ISAE 3402-audit
- **Cost Management** → Uniserver rapporteert maandelijks verbruik per klant via het MijnUniserver-portaal

Het verschil: bij Uniserver is **datasoevereiniteit** altijd het eerste governance-criterium. CAF heeft hier minder aandacht voor dan voor public cloud-compliance.

---

## Is CAF compleet?

**Sterktes:**
- Diepgaande aandacht voor de meest voorkomende governance-problemen: kosten, security, identity
- Azure Landing Zones bieden governance-as-code — direct inzetbaar
- Regelmatig bijgewerkt door Microsoft
- Gratis toegankelijk

**Beperkingen:**
- Sterk Azure-gericht — beperkt bruikbaar voor multi-cloud of private cloud
- Omvangrijke documentatie kan overweldigend zijn voor kleine organisaties
- Geavanceerde implementatie vereist Bicep/Terraform kennis

---

## Hoe gaan cloudproviders om met vergelijkbare frameworks?

Alle grote cloudproviders hebben een equivalent framework:

| Provider | Framework |
|----------|-----------|
| Microsoft Azure | Cloud Adoption Framework (CAF) |
| Amazon AWS | AWS Cloud Adoption Framework (AWS CAF) |
| Google Cloud | Google Cloud Architecture Framework |

De kernprincipes zijn vergelijkbaar: strategy → plan → adopt → govern → manage. Het feit dat alle drie de hyperscalers een vergelijkbaar model hanteren bevestigt dat CAF de industrie-standaard vertegenwoordigt.

---

## Mijn persoonlijke mening

Als System Administrator bij Uniserver werk ik dagelijks met de uitdagingen die CAF probeert op te lossen. Wat mij het meest aanspreekt aan het framework is de pragmatische aanpak: het begint niet met technologie maar met de vraag *waarom* je naar de cloud wilt. Zonder een duidelijk antwoord op die vraag zie ik in de praktijk dat organisaties cloudprojecten starten die na een jaar vastlopen omdat kosten of beveiliging niet goed zijn geregeld.

De vijf governance-disciplines van CAF sluiten nauw aan bij de problemen die ik dagelijks zie. Kostenbeheersing is bij Uniserver cruciaal: klanten die onverwacht hoge facturen krijgen omdat resources niet zijn opgeruimd, of omdat niemand overzicht had over het totale verbruik. CAF's Cost Management discipline — met budgets, tags en FinOps-reviews — is precies wat dit soort situaties voorkomt.

Wat ik minder sterk vind aan CAF is dat het soms voelt als een Microsoft-verkooppraatje. Elke aanbeveling leidt naar een Azure-dienst. Voor organisaties die multi-cloud of sovereign cloud willen, zoals Uniserver, moet je de principes vertalen naar je eigen context. Dat vraagt extra denkwerk.

Toch zou ik CAF aanbevelen aan elke organisatie die serieus aan cloudadoptie begint. Niet als strak te volgen handleiding, maar als referentiekader om structuur aan te brengen in een complex vraagstuk. Je hoeft niet alles te implementeren — zelfs de eerste drie disciplines (Cost, Security, Resource Consistency) geven al enorm veel grip op een onbeheerste cloudomgeving. De beschikbaarheid als open-source framework zonder licentiekosten maakt de drempel bovendien laag. Voor studenten en professionals die zich willen verdiepen in cloud governance is CAF een uitstekend startpunt.

---

## Conclusie

Het Microsoft Cloud Adoption Framework is een praktisch en uitgebreid governance-raamwerk dat organisaties helpt cloudadoptie gestructureerd aan te pakken. De Govern-fase met de vijf disciplines (Cost, Security, Resource Consistency, Identity, Deployment Acceleration) vormt een solide basis voor elke cloud governance-strategie.

Voor organisaties die met Azure werken is CAF de logische keuze. Voor sovereign cloud providers zoals Uniserver zijn de principes waardevol, maar vereisen aanpassing aan een private cloud context.

---

## Bronnen

- Microsoft. (2024). *Cloud Adoption Framework voor Azure*. https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/
- Microsoft. (2024). *Azure Landing Zones*. https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/
- Amazon Web Services. (2024). *AWS Cloud Adoption Framework*. https://aws.amazon.com/cloud-adoption-framework/
- Google Cloud. (2024). *Google Cloud Architecture Framework*. https://cloud.google.com/architecture/framework
- van der Ploeg, R. (2024). *Cloud Governance Workbook TICT-CDU4GOV-24*. Hogeschool Utrecht.
