import { Img2 } from "../assets";
import styles, { layout } from "../style";

const Billing = () => (
  <section id="product" className={layout.sectionReverse}>
    <div className={layout.sectionImgReverse}>
      <img src={Img2} alt="billing" className="w-[100%] h-[95%] relative z-[5]" />

      {/* gradient start */}
      <div className="absolute z-[3] -left-1/2 top-0 w-[50%] h-[50%] rounded-full white__gradient" />
      <div className="absolute z-[0] w-[50%] h-[50%] -left-1/2 bottom-0 rounded-full pink__gradient" />
      {/* gradient end */}
    </div>

    <div className={layout.sectionInfo}>
      <h2 className={styles.heading2}>
        Beneficios <br className="sm:block hidden" />
      </h2>
      <p className={`${styles.paragraph} max-w-[470px] mt-5`}>

        Nuestra solución ofrece múltiples beneficios significativos. En primer lugar, optimizamos el riego y reducimos el desperdicio de agua, lo que garantiza un uso más eficiente de este recurso vital. Además, promovemos prácticas agrícolas sostenibles y la conservación de recursos hídricos, asegurando así un futuro más verde. Gracias a la tecnología blockchain, nuestros datos son inmutables y transparentes, proporcionando una trazabilidad completa. También ofrecemos predicciones climáticas precisas, lo que permite ajustar las prácticas agrícolas y adaptarse mejor a las condiciones cambiantes del clima. Finalmente, capacitamos a los agricultores en la gestión y conservación del agua, fomentando un uso responsable y consciente de este recurso esencial.
      </p>


    </div>
  </section>
);

export default Billing;
