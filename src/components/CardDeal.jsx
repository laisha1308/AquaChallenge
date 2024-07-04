import { Img1 } from "../assets";
import styles, { layout } from "../style";
import Button from "./Button";

const CardDeal = () => (
  <section className={layout.section}>
    <div className={layout.sectionInfo}>
      <h2 className={styles.heading2}>
        Visión y Misión <br className="sm:block hidden" />
      </h2>
      <p className={`${styles.paragraph} max-w-[470px] mt-5`}>
        Nuestra Visión: Aspiramos a transformar la agricultura con tecnología innovadora que promueva la sostenibilidad y la eficiencia en el uso de los recursos naturales.
        <br />
        Nuestra Misión: Nos dedicamos a proporcionar soluciones tecnológicas avanzadas que empoderen a los agricultores, ayudándoles a enfrentar los desafíos del cambio climático y asegurar la sostenibilidad de sus prácticas agrícolas.      </p>

    </div>

    <div className={layout.sectionImg}>
      <img src={Img1} alt="billing" className="w-[100%] h-[100%]" />
    </div>
  </section>
);

export default CardDeal;
