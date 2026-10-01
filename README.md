# TP CI/CD avec GitHub Actions, Docker et Python

Ce projet démontre la mise en place d'une pipeline d'intégration et de déploiement continus (CI/CD) entièrement automatisée pour une API Python.

## Fonctionnement du pipeline

À chaque `push` sur la branche `main`, le workflow GitHub Actions s'exécute avec les étapes suivantes :
1. **Unit tests** : Exécution isolée des tests unitaires via `pytest`.
2. **E2E tests** : Tests des endpoints HTTP avec le `TestClient` de FastAPI.
3. **Build & Push** : Si les tests passent, l'image Docker est construite puis poussée sur Docker Hub.
4. **Deploy** : Connexion SSH à la VM Azure, rapatriement de la nouvelle image, redémarrage idempotent du conteneur et vérification du service (healthcheck).

## Choix techniques réalisés

* **Python & FastAPI** : Framework moderne, rapide et simple pour exposer des endpoints.
* **Pytest** : Le standard pour les tests en Python, permettant d'exécuter facilement les tests unitaires et E2E en CI.
* **Idempotence du déploiement** : L'utilisation de `docker stop myapp || true` suivi de `docker rm` permet de relancer la pipeline à volonté sans erreur de port ou de conflit de nom.
* **Sécurité** : Utilisation exclusive de *GitHub Secrets* pour les clés SSH, IP, et credentials Docker Hub, aucun identifiant n'est exposé dans le code.