import styles from "../style";


const CTA = () => (
  <section className={`${styles.flexCenter} ${styles.marginY} ${styles.padding} sm:flex-row flex-col bg-black-gradient rounded-[20px] box-shadow `}>
    <div className="flex-1 flex flex-col">
      <h2 className={`${styles.heading2} text-white`}>Únete a Nosotros</h2>
      <p className={`${styles.paragraph} text-white max-w-[600px] mt-2`}>
        Creemos que la innovación y la tecnología pueden transformar la agricultura y contribuir a un uso más sostenible del agua. Únete a nosotros en este proyecto y juntos aseguraremos un futuro más verde y sostenible para todos.
      </p>
    </div>

    <div className={`${styles.flexCenter} sm:ml-10 ml-0 sm:mt-0 mt-10`}>

    </div>
  </section>
);

export default CTA;