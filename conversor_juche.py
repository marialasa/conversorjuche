def conversor_juche():

    while True:

      try:
          gregoriano = int(input("Ingresá un año del calendario gregoriano y presioná enter: "))
          juche = gregoriano - 1911

      except ValueError:
          print("Ingresá un año válido en formato numérico.")
          continue

      if gregoriano >= 1912 and gregoriano <= 2023:
          print(f"El año {gregoriano} del calendario gregoriano equivale al año {juche} del calendario Juche.")

      elif gregoriano >= 2024:
          print(f"El año {gregoriano} del calendario gregoriano, en un futuro, equivaldría al año {juche} del calendario Juche.")

      else:
          print("Los años anteriores a 1912, en Corea del Norte, se computan en calendario gregoriano.")
          print("En el calendario Juche no existe ni el año 0 ni el equivalente al a.C.")

      loop = input("¿Querés convertir otro año? Sí o No: ")

      if loop.lower() in ["no", "n"]:
          print("📅 ¡Muchas gracias por usar el conversor Juche! 📅")
          break

    return None

conversor_juche()
