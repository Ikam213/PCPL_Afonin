use std::io;

fn get_coef(prompt: &str) -> f64 {
    let mut input = String::new();
    println!("{}", prompt);
    io::stdin().read_line(&mut input).expect("A string");
    return input.trim().parse::<f64>().expect("Введено не число!");
}

fn get_roots(a: f64, b: f64, c: f64) -> Vec<f64>{
    let mut roots_list = Vec::<f64>::new();
    let d: f64 = b*b - 4.0*a*c;
    if d == 0.0 {
        if -b/(2.0*a) > 0.0 {
            let root1: f64 = f64::sqrt(-b/(2.0*a) as f64);
            let root2: f64 = -root1;
            roots_list.push(root1);
            roots_list.push(root2);
        }
        else if (a != 0.0) && (b == 0.0) {
            let root1: f64 = 0.0;
            roots_list.push(root1)
        }
    }
    if d > 0.0 {
        let buf1: f64 = (-b - f64::sqrt(d as f64))/(2.0*a);
        let buf2: f64 = (-b + f64::sqrt(d as f64))/(2.0*a);
        if buf1 > 0.0 {
            let root1: f64 = f64::sqrt(buf1 as f64);
            let root2: f64 = -root1;
            roots_list.push(root1);
            roots_list.push(root2);
        }
        else if buf1 == 0.0 {
            let root1: f64 = 0.0;
            roots_list.push(root1);
        }
        if buf2 > 0.0 {
            let root3: f64 = f64::sqrt(buf2 as f64);
            let root4: f64 = -root3;
            roots_list.push(root3);
            roots_list.push(root4);
        }
        else if buf2 == 0.0 {
            let root3: f64 = 0.0;
            roots_list.push(root3);
        }
    }
    return roots_list;
}

fn main() {
    let a = get_coef("Введите коэффициент а: ");
    let b = get_coef("Введите коэффициент b: ");
    let c = get_coef("Введите коэффициент c: ");
    let roots = get_roots(a, b, c);
    let len_roots = roots.len();
    if len_roots == 0 {
        println!("Корней нет");
    } else if len_roots == 1 {
        println!("Один корень: {}", roots[0]);
    } else if len_roots == 2 {
        println!("Два корня: {} и {}", roots[0], roots[1]);
    } else if len_roots == 3 {
        println!("Три корня: {} и {} и {}", roots[0], roots[1], roots[2]);
    } else {
        println!("Четыре корня: {} и {} и {} и {}", roots[0], roots[1], roots[2], roots[3]);
    }
}