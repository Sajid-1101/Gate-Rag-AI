from langchain_community.document_loaders import PyPDFLoader

import os


def load_all_pdfs(folder_path):

    documents = []

    failed_files = []


    for file in os.listdir(folder_path):

        if file.endswith(".pdf"):

            try:

                pdf_path = os.path.join(
                    folder_path,
                    file
                )


                print(
                    "Loading:",
                    file
                )


                loader = PyPDFLoader(
                    pdf_path
                )


                pages = loader.load()


                print(
                    "Pages:",
                    len(pages)
                )


                documents.extend(
                    pages
                )


            except Exception as e:

                print(
                    "Skipping corrupted PDF:",
                    file
                )

                failed_files.append(file)


    print("\nFailed PDFs:")

    for file in failed_files:

        print(file)


    return documents