def main_menu():
  print("WELCOME TO STREAMTREE")
  print("\nMenu:")
  print("1. Add video")
  print("2. Remove video")
  print("3. Find recommended")
  print("4. Add video ke Queue")
  print("5. Remove video dari Queue")
  print("6. Exit")
  print()

  try:
    choice = int(input("Pilih menu : "))
    if choice == 1:
      print("Fungsi Add video dipilih.")
    elif choice == 2:
      print("Fungsi Remove video dipilih.")
    elif choice == 3:
      print("Fungsi Find recommended dipilih.")
    elif choice == 4:
      print("Fungsi Add video ke Queue dipilih.")
    elif choice == 5:
      print("Fungsi Remove video dari Queue dipilih.")
    elif choice == 6:
      print("Terima kasih sudah menggunakan StreamTree. Sampai jumpa!")
      return False
    else:
      print("Pilihan tidak valid. Silakan coba lagi.")
  except ValueError:
    print("Input tidak valid")
  return True

if __name__ == "__main__":
  while main_menu():
    print("\n")