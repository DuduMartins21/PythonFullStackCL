class hotel {
    constructor(nome, cidade, quartosDisponiveis) {
        this.nome = nome;
        this.cidade = cidade;
        this.quartosDisponiveis = quartosDisponiveis;   
    }
    reservarQuarto() {
        if (this.quartosDisponiveis > 0) {
            this.quartosDisponiveis--;
            console.log(`Quarto reservado no ${this.nome} em ${this.cidade}.`);
            return true;
        } else {
            console.log(`Desculpe, não a quartos disponiveis no ${this.nome}.`);
        }
    }
    cancelarReserva() {
        this.quartosDisponiveis++;
        console.log(`Reserva cancelada no ${this.nome}.`);
    }
}

class cliente {
    constructor(nome, CPF) {
        this.nome = nome;
        this.CPF = CPF;
        this.historicoReservas = [];
    }

    reservarQuarto(hotel) {
        const sucessoReserva = hotel.reservarQuarto();  // Tenta fazer a reserva no hotel
        if (sucessoReserva) {
            this.historicoReservas.push(`Reserva no ${hotel.nome}, cidade: ${hotel.cidade}`);
        }
    }

    cancelarReserva(hotel) {
        hotel.cancelarReserva();
        const indiceReserva = this.historicoReservas.findIndex(reserva => reserva.includes(hotel.nome));
        if (indiceReserva !== -1) {
            this.historicoReservas.splice(indiceReserva, 1);  // Remove a reserva cancelada do histórico
        }
    }

    verHistorico() {
        console.log(`${this.nome}, Historicos de Reservas: `)
        if (this.historicoReservas.length === 0) {
            console.log("nenhuma reserva feita.")
        } else {
            this.historicoReservas.forEach(reserva => {
                console.log(reserva);
            });
                
        }
    }
}


const hotel1 = new Hotel("Fluminense", "Rio de Janeiro", 5);
const hotel2 = new Hotel("Vasco", "Cantão RJ", 2);

const cliente1 = new Cliente("Carlos Eduardo", "123.456.789-21");
const cliente2 = new Cliente("Alyfer Mateus", "171.157.155-69");

cliente1.reservarQuarto(hotel1);

cliente2.reservarQuarto(hotel2);

cliente1.verHistorico();
cliente2.verHistorico();

cliente1.cancelarReserva(hotel1);
    
cliente1.verHistorico();
hotel1.quartosDisponiveis;