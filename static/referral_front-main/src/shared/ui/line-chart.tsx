import { useEffect, useRef } from "react";
import { select, line, scaleLinear, extent } from "d3";
import useMeasure from "react-use-measure";

export const LineChart = ({ data }: { data: number | string[][] }) => {
    // const data = [
    //     [0, 0],
    //     [10, 10],
    //     [30, 15],
    //     [35, 20],
    //     [45, 25],
    //     [100, 200]
    // ];

    const [ref, bounds] = useMeasure();

    return (
        <div
            className="aspect-[785_/_595] min-h-[460px] w-full md:aspect-[640_/_240]"
            ref={ref}
        >
            {bounds.width > 0 ? (
                <Chart
                    data={data}
                    width={bounds.width}
                    height={bounds.height}
                />
            ) : null}
        </div>
    );
};

const Chart = ({
    data,
    width,
    height
}: {
    data: any;
    width: number;
    height: number;
}) => {
    const chartRef = useRef<SVGSVGElement>(null);

    const margin = {
        top: 20,
        right: 20,
        bottom: 20,
        left: 40
    };

    const yExtent = extent(data?.map((d: number[][]) => d[1]));

    const xScale = scaleLinear()
        .domain(extent(data.map(d => d[0])))
        .range([margin.left, width - margin.right]);

    const yScale = scaleLinear()
        .domain(yExtent)
        .range([height - margin.bottom, margin.top]);

    const lineChart = line()
        .x(data => xScale(data[0]))
        .y(data => yScale(data[1]));

    const d = lineChart(data);

    useEffect(() => {
        const chart = select(chartRef.current);

        chart
            .select(".xAxis")
            .attr("x1", margin.left)
            .attr("y1", margin.top)
            .attr("x2", margin.left)
            .attr("y2", height - margin.bottom)
            .attr("fill", "none")
            .attr("stroke", "currentColor")
            .attr("stroke-width", "0.5");

        chart
            .select(".yAxis")
            .attr("x1", margin.left)
            .attr("y1", height - margin.bottom)
            .attr("x2", width - margin.right)
            .attr("y2", height - margin.bottom)
            .attr("fill", "none")
            .attr("stroke", "currentColor")
            .attr("stroke-width", "0.5");
    }, [height, width]);

    return (
        <svg
            width={width}
            height={height}
            viewBox={`0 0 ${width} ${height}`}
            ref={chartRef}
        >
            <path
                d={d}
                fill="none"
                stroke="#FF8551"
                strokeWidth="5"
            />

            <line className="xAxis" />
            <line className="yAxis" />

            {xScale
                .ticks(5)
                // .slice(1)
                .map(tick => (
                    <line
                        x1={xScale(tick)}
                        y1={margin.top}
                        x2={xScale(tick)}
                        y2={height - margin.bottom}
                        stroke="currentColor"
                        strokeWidth="0.25"
                        opacity="0.7"
                    />
                ))}

            {yScale.ticks(5).map(tick => (
                <g
                    key={tick}
                    transform={`translate(0,${yScale(tick)})`}
                >
                    <line
                        x1={margin.left}
                        x2={width - margin.right}
                        stroke="currentColor"
                        strokeWidth="0.25"
                        opacity="0.7"
                    />
                    <text
                        // y={-5}
                        x={30}
                        fill="currentColor"
                        alignmentBaseline="middle"
                        textAnchor="end"
                        className="font-primary text-xs-base-xs-lg"
                    >
                        {tick}
                    </text>
                </g>
            ))}
        </svg>
    );
};
