import { Search } from "lucide-react";
function NavBar() {
  return (
    <>
      <div className="navbar rounded-[2rem] flex flex-row p-3 justify-between">
        <div className="flex flex-row gap-2 mt-1">
          <input
            type="text"
            placeholder="search..."
            className="searchbar rounded-xl p-2 text-white font-semibold"
          />
          <Search className="text-white mt-2" />
        </div>
        <div className="text-orange-500 mt-2 text-3xl font-bold">Dotanalytics</div>
      </div>
    </>
  );
}

export default NavBar;
