import { features } from "../constants";
import styles, { layout } from "../style";
import Button from "./Button";

const FeatureCard = ({ icon, title, content, index }) => (
  <div className={`flex flex-row p-6 rounded-[20px] cursor-pointer ${index !== features.length - 1 ? "mb-6" : "mb-0"} `}>
    <div className={`w-[64px] h-[64px] rounded-full ${styles.flexCenter} bg-green-icon`}>
      <img src={icon} alt="" className="w-[50%] h-[50%] object-contain" />
    </div>
    <div className="flex-1 flex flex-col ml-3">
      <h4 className="font-poppins font-semibold text-black text-[18px] leading-[23.4px] mb-1">
        {title}
      </h4>
      <p className="font-poppins font-normal text-black text-[16px] leading-[24px]">
        {content}
      </p>
    </div>
  </div>
);

const Business = () => (
  <section id="features" className={layout.section}>
    <div className={layout.sectionInfo}>
      <h2 className={styles.heading2}>
        HidroVerde: <br className="sm:block hidden " />
        Transformando el Riego, Conservando el Futuro
      </h2>
      <p className={`${styles.paragraph} max-w-[470px] mt-5`}>
        El cambio climático ha incrementado las temperaturas y prolongado los períodos de sequía,
        dificultando las prácticas agrícolas y poniendo en riesgo la sostenibilidad de los cultivos.
        El agua es un recurso esencial para la agricultura, y su gestión eficiente es crucial para
        garantizar la productividad y la sostenibilidad.
      </p>


    </div>

    <div className={`${layout.sectionImg} flex-col`}>
      <h2 className="font-poppins font-semibold xs:text-[30px] text-[20px] text-black">Solución Tecnológica</h2>
      {features.map((feature, index) => (
        <FeatureCard key={feature.id} {...feature} index={index} />
      ))}
    </div>
  </section>
);

export default Business;
