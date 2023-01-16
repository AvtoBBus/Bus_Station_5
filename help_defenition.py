def search_pdf_in_list(input_list: list) -> bool:
    find = False
    for elem in input_list:
        if str(elem)[-4:].find("pdf") == -1:
            pass
        else:
            find = True
    return find
