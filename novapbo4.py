class vehicle:
    def __init__(self, brand, model):
        if brand == "" or model == "":
            raise ValueError("brand dan model tidak boleh kosong")

        self.brand = brand
        self.model = model

    def drive(self):
        print(f"The {self.brand} {self.model} is driving.")


class car(vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)

        if doors <= 0:
            raise ValueError("jumlah pintu tidak boleh nol atau negatif")

        self.doors = doors

    def honk(self):
        print("Beep! Beep!")


class truck(vehicle):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        self.load_capacity = load_capacity

    def load(self, weight):
        if weight > self.load_capacity:
            print("Error: Muatan melebihi kapasitas truck")
        else:
            print(f"Loaded {weight} kg.")


def main():
    print("=== program simulasi kendaraan ===\n")

    my_car = car("toyota", "corolla", 4)
    print("mobil berhasil dibuat:", my_car.brand, my_car.model, f"({my_car.doors} pintu)")

    print("\n--- aktivitas mobil ---")
    my_car.drive()
    my_car.honk()

    my_truck = truck("ford", "F-150", 1000)
    print("\nTruk berhasil dibuat:", my_truck.brand, my_truck.model)
    print("kapasitas muatan:", my_truck.load_capacity, "kg")

    print("\n--- aktivitas truk ---")
    my_truck.drive()
    my_truck.load(500)
    my_truck.load(1200)

    print("\n=== program selesai ===")


if __name__ == "__main__":
    main()