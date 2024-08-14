import { TypedUseSelectorHook, useSelector } from "react-redux";
import { RootStore } from "../types";

export const useStateSelector: TypedUseSelectorHook<RootStore> = useSelector;
