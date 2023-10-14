## Rust (linguaggio di programmazione)

#### Domanda 1. Quale tipo cast preserva il valore matematico in tutti i casi?

- [ ] i64 come i32
- [ ] usa come u64
- [x] i32 come i64
- [ ] f64 come f32

#### Domanda 2. Cosa rappresentano le barre verticali qui?

"ruggine".
str::thread::spawn(|| {
println!("LinkedIn");
});

```

- [x] una chiusura
- [ ] un filo
- [ ] un futuro
- [ ] un blocco

[riferimento](https://doc.rust-lang.org/book/ch13-01-closures.html#refactoring-with-closures-to-store-code)

#### Domanda 3. Quale scelta non è un tipo di dati scalare?

- [ ] numero intero
- [ ] galleggiante
- [ ] booleano
- [x] tupla

#### Q4. **\_** non è destrutturabile.

- [x] Tratti
- [ ] Tuple
- [ ] Enumerazioni
- [ ] Strutture

[riferimento](https://rust-lang.github.io/rfcs/2909-destructuring-assignment.html)

#### D5. Quale comando "cargo" controlla la presenza di errori in un programma senza creare un eseguibile binario?

- [ ] carico --versione
- [ ] carico init
- [] costruzione del carico
- [x] controllo del carico

#### Domanda 6. Il termine _box_ e frasi correlate come _boxing a value_ vengono spesso utilizzate quando si parla di layout della memoria. A cosa si riferisce _box_?

- [ ] Sta creando un puntatore sull'heap che punta a un valore nello stack.
- [x] Sta creando un puntatore nello stack che punta a un valore nell'heap.
- [ ] Sta creando una guardia della memoria attorno ai valori per impedire l'accesso illegale.
- [ ] È un'astrazione che si riferisce alla proprietà. I valori "riquadro" sono chiaramente etichettati.

#### Domanda 7. Qual è un modo alternativo di scrivere "slice" che produce lo stesso risultato?

"ruggine".
...
let s = String::form("ciao");
let fetta = &s[0..2];
```

- [ ] let fetta = &s[len + 2];
- [ ] let fetta = &s[len - 2];
- [ ] let slice = &s.copy(0..2);
- [x] lascia fetta = &s[..2];

#### Domanda 8. Usare l'operatore `?` alla fine di un'espressione equivale a **\_**.

- [ ] un modello di corrispondenza che si ramifica in Vero o Falso
- [ ] chiamando ok_error()
- [ ] chiamando il panico!()
- [x] uno schema di corrispondenza che potrebbe comportare una restituzione anticipata

#### Domanda 9. Qual è la sintassi valida per definire un array di valori i32?

- [ ] Array<i32>::con_capacità(10)
- [ ] [i32]
- [ ] Array<i32>::new(10)
- [x] [i32; 10]

#### D10. Quale sintassi è richiesta per prendere un riferimento mutabile a T, quando utilizzato all'interno di un argomento di funzione?

"ruggine".
fn incremento(i: T) {
// corpo eliso
}

```

- [ ] \*mut T
- [ ] mut rif T
- [ ] muto &T
- [x] &mut T

#### Domanda11. I puntatori intelligenti Rc e Arc forniscono il conteggio dei riferimenti. Qual è l'API per incrementare un conteggio dei riferimenti?

- [ ] .aggiungere()
- [ ] .incr()
- [x] .clone()
- [ ] .incremento()

[riferimento](https://doc.rust-lang.org/book/ch15-04-rc.html)

#### Domanda12. Cosa succede quando si verifica un errore gestito dall'operatore punto interrogativo (?)?

- [ ] L'errore viene segnalato e l'esecuzione continua.
- [ ] Viene sollevata un'eccezione. Gli effetti dell'eccezione sono definiti dall'errore! macro.
- [ ] Il programma va immediatamente nel panico.
- [x] Rust tenta di convertire l'errore nel tipo di errore della funzione locale e lo restituisce come Risultato::Err. Se fallisce, il programma va nel panico.

#### Domanda 13. Quale sintassi dei commenti non è legale?

- [ ] `/*`
- [x] `#`
- [ ] `//!`
- [ ] `//`

#### Domanda14. Nei modelli corrispondenti, i valori vengono ignorati con \_.

- [ ] `.ignore()`
- [ ] `un carattere di sottolineatura (_)`
- [X] ..
- [ ] saltare

#### D15. La definizione di \_ richiede un parametro di durata.

- [ ] funzione che termina la durata di uno dei suoi argomenti
- [x] struttura che contiene un riferimento a un valore
- [ ] funzione con un argomento generico
- [ ] struttura che contiene un riferimento a un valore boxed

[Riferimento al libro Rust](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html#lifetime-annotations-in-struct-definitions)

#### Domanda 16. Quale esempio utilizza correttamente l'API Entry di std::collections::HashMap per popolare i conteggi?

"ruggine".
usa std::collections::HashMap;
fn principale() {
     lascia che mut conti = HashMap::new();
     let text = "LinkedIn Learning";
     per c in text.chars() {
         // Completa questo blocco
     }
     println!("{:?}", conta);
}
```

- [ ] &Timido;

"ruggine".
per c in text.chars() {
if let Some(count) = &mut counts.get(&c) {
conta.inserisci(c, \*conta + 1);
} altro {
conta.inserisci(c, 1);
};
}

```

- [x] &timido;

"ruggine".
per c in text.chars() {
     let count = counts.entry(c).or_insert(0);
     *conta += 1;
}
```

- [ ] &Timido;

"ruggine".
per c in text.chars() {
lascia contare = conta.voce(c);
\*conta += 1;
}

```

- [ ] &Timido;

"ruggine".
per c in text.chars() {
     conta.entry(c).or_insert(0).map(|x| x + 1);
}
```

[riferimento](https://doc.rust-lang.org/std/collections/hash_map/struct.HashMap.html#method.entry)

#### D17. Quale frammento non comporta allocazioni di memoria durante la scrittura su un "file" (rappresentato da un Vec<u8>)?

"ruggine".
usa std::collections::HashMap;

fn main() -> Risultato<(), Box<dyn std::error::Error>> {
let mut v = Vec::<u8>::new();

     let a = "LinkedIn";
     sia b = 123;
     sia c = '🧀';

     // sostituisci questa riga

     println!("{:?}", v);

     OK(())

}

```

- [X] :

"ruggine".
scrivi!(&mut v, "{}{}{}", a, b, c)?;
```

- [ ] :

"ruggine".
v.scrivere(a)?;
v.scrivere(b)?;
v.scrivere(c)?;

```

- [ ] :

"ruggine".
```
