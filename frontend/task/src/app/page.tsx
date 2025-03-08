import Jogos from "./jogo/components/jogos";

import ClubesList from "./components/clubes";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 max-w-5xl w-full items-top justify-between font-mono text-sm lg:flex gap-2.5">
        <ClubesList />
        <Jogos />
      </div>
    </main>
  );
}
