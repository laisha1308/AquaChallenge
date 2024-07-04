import styles from "../style";
import { discount, heroImg } from "../assets";
import GetStarted from "./GetStarted";


const Hero = () => {
  return (
    <section id="home" className={`flex md:flex-row flex-col ${styles.paddingY}`}>
      <div className={`flex-1 ${styles.flexStart} flex-col xl:px-0 sm:px-16 px-6`}>

        <div className="flex flex-row justify-between items-center w-full">
          <h1 className="flex-1 font-poppins font-semibold ss:text-[65px] text-[45px] text-black ss:leading-[100.8px] leading-[75px]">
            Riego Inteligente <br className="sm:block hidden" />{" "} para un Mundo más
            <span className="text-gradient">  Verde  </span>{" "}
          </h1>
          <div className="ss:flex hidden md:mr-4 mr-0">
            <GetStarted />
          </div>
        </div>
        <h1 className="font-poppins font-semibold ss:text-[68px] text-[52px] text-black ss:leading-[100.8px] leading-[75px] w-full">
        </h1>

        <p className={`${styles.paragraph} text-black max-w-[550px] mt-3`}>
          HidroVerde es una herramienta innovadora que combina tecnologías como loT, Redes Neuronales y Blockchain, con el objetivo de optimizar el uso del agua en la agricultura. Sensores en campo recopilan datos en tiempo real, estos datos alimentan una red neuronal que predice patrones climáticos como precipitación, calcula las necesidades de agua en el cultivo y ajusta automáticamente el sistema riego.
          Esta solución mejora la eficiencia del recurso hídrico, promueve prácticas sostenibles y ayuda a los agricultores a enfrentar los efectos adversos del cambio climático como las sequías prolongadas o las lluvias intensas.
        </p>

      </div>

      <div className={`flex-1 flex ${styles.flexCenter} md:my-0 my-10 relative`}>
        <img src={heroImg} alt="billing" className=" w-[100%] h-[95%] relative z-[5]" />

        {/* gradient start */}
        <div className="absolute z-[0] w-[40%] h-[35%] top-0 pink__gradient" />
        <div className="absolute z-[1] w-[80%] h-[80%] rounded-full white__gradient bottom-40" />
        <div className="absolute z-[0] w-[50%] h-[50%] right-20 bottom-20 blue__gradient" />
        {/* gradient end */}
      </div>

      <div className={`ss:hidden ${styles.flexCenter}`}>
        <GetStarted />
      </div>
    </section>
  );
};

export default Hero;
