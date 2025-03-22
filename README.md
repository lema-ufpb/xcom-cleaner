# Airflow DAG Module

## XCOM History Cleaner

This project implements a pipeline to clean the history of XCOM variables stored by Airflow.

---

## License

The information contained herein is confidential and proprietary to the research group.

Use, copying, transfer, or disclosure of this information without the owner's consent is prohibited.

ALL RIGHTS RESERVED
(c) 2023 LEMA-UFPB.
João Pessoa, PB, Brazil

---

## Prerequisites

Tools:

- [Docker](https://www.docker.com/)
- [Apache Airflow](https://airflow.apache.org/)

---

## ☢️ Best Practices

- Never save sensitive credential data in GitLab (even if encrypted).
- Review code and apply linting before pushing.
- Use the task or feature code in the commit message. Ex: `git commit -m "task/01: message ..."`.
- Open a merge request to the `main` branch and request a reviewer.

---

## 📦 Test Environment

- Agile Development

In VSCode, execute tests in **Airflow via command line** using the F5 key. Tasks have been configured in the `.vscode` directory for pre-checking the Docker environment for local execution of the data pipeline.

- Access the Airflow Webserver at [http://localhost:8080](http://localhost:8080)

---

## 🔗 Related Links

- [How to Design Better DAGs in Apache Airflow](https://towardsdatascience.com/how-to-design-better-dags-in-apache-airflow-494f5cb0c9ab)
- [Apache Airflow Best Practices and Advantages](https://medium.com/digital-transformation-and-platform-engineering/apache-airflow-best-practices-and-advantages-9ec71f1ef3cc)
- [Best Practices - Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html)
- [Apache Airflow – How to write DAGs and master all best practices](https://itgix.com/blog/apache-airflow-how-to-write-dags-and-master-all-best-practices/)

## 👏 Contacts and Acknowledgments

- hilton.martins@academico.ufpb.br
- alessio.almeida@academico.ufpb.br
