/* -------------------------------------------------------------------------
 *  A repertory of multi primitive-to-primitive (MP2P) ICP algorithms in C++
 * Copyright (C) 2018-2021 Jose Luis Blanco, University of Almeria
 * See LICENSE for license information.
 * ------------------------------------------------------------------------- */

/**
 * @file   render_params.h
 * @brief  Render parameters for the different geometric entities
 * @author Jose Luis Blanco Claraco
 * @date   March 26, 2021
 */
#pragma once

#include <mp2p_icp/layer_name_t.h>
#include <mrpt/img/TColor.h>
#include <mrpt/img/color_maps.h>
#include <mrpt/opengl/opengl_frwds.h>
#include <mrpt/typemeta/TEnumType.h>

#include <map>
#include <optional>
#include <vector>

namespace mp2p_icp
{
/** \addtogroup mp2p_icp_grp
 * @{
 */

/** Used in metric_map_t::get_visualization() */
struct render_params_planes_t
{
    render_params_planes_t() = default;

    bool              visible     = true;
    double            halfWidth   = 1.0;
    double            gridSpacing = 0.25;
    mrpt::img::TColor color{0xff, 0xff, 0xff, 0xff};
};

/** Used in metric_map_t::get_visualization() */
struct render_params_lines_t
{
    render_params_lines_t() = default;

    bool              visible = true;
    mrpt::img::TColor color{0xff, 0x00, 0x00, 0xff};
    double            length = 20.0;  //!< all lines with same length
    std::optional<std::vector<double>> lengths;  //!< individual lengths
};

enum class Coordinate : uint8_t
{
    X = 0,
    Y,
    Z
};

struct color_mode_t
{
    /** The colormap palette to use. */
    mrpt::img::TColormap colorMap = mrpt::img::cmHOT;

    /** If set, the coordinate to use to recolorize points. */
    std::optional<Coordinate> recolorizeByCoordinate;

    /** Optional fixed minimum and maximum bounding box limits for
     *  interpolating the color map. If not set, they will be set to the point
     * cloud bounding box.
     * For example, to recolor points so the coolest and hottest colors are
     * at heights of 0.0 m and 5.0 m, respectively, set these variables to 0.0f
     * and 5.0f and set the mrpt::img::cmHOT color map.
     */
    std::optional<float> colorMapMinCoord, colorMapMaxCoord;
};

/** Rendering options for each point layer, see
 * metric_map_t::get_visualization() */
struct render_params_point_layer_t
{
    render_params_point_layer_t() = default;

    /** Point size, in pixels (can be fractional). Zooming in (very close) into
     * points show them as square patches. */
    float pointSize = 1.0f;

    /** Fixed color for all points in the layer. Ignored if colorMode is set. */
    mrpt::img::TColor color{0x00, 0x00, 0xff, 0xff};

    /** If set, it overrides `color` and defines a "recolorize by coordinate"
     * mode. */
    std::optional<color_mode_t> colorMode;
};

/** Used in metric_map_t::get_visualization() */
struct render_params_points_t
{
    render_params_points_t() = default;

    /** If false, all other options are ignored and no points will be rendered.
     */
    bool visible = true;

    /** Used only if `perLayer` is empty, this defines common parameters for all
     * layers. */
    render_params_point_layer_t allLayers;

    /** If not empty, only the layers defined as keys will be visible, each one
     * with its own set of parameters. */
    std::map<layer_name_t, render_params_point_layer_t> perLayer;
};

/** Used in metric_map_t::get_visualization() */
struct render_params_t
{
    render_params_t() = default;

    render_params_planes_t planes;
    render_params_lines_t  lines;
    render_params_points_t points;
};

struct render_params_pairings_pt2pt_t
{
    render_params_pairings_pt2pt_t() = default;

    bool visible = true;

    mrpt::img::TColor color{0x80, 0x80, 0x80, 0xa0};
};

struct render_params_pairings_pt2pl_t
{
    render_params_pairings_pt2pl_t() = default;

    bool visible = true;

    mrpt::img::TColor segmentColor{0x00, 0xff, 0x00, 0xa0};
    mrpt::img::TColor planePatchColor{0x00, 0xff, 0x00, 0x80};
    double            planePatchSize = 0.2;
};

struct render_params_pairings_pt2ln_t
{
    render_params_pairings_pt2ln_t() = default;

    bool visible = true;

    mrpt::img::TColor segmentColor{0x00, 0xff, 0x00, 0xa0};
    mrpt::img::TColor lineColor{0x00, 0xff, 0x00, 0x80};
    double            lineLength = 0.2;
};

/** Used in Pairings::get_visualization() */
struct pairings_render_params_t
{
    pairings_render_params_t() = default;

    render_params_pairings_pt2pt_t pt2pt;
    render_params_pairings_pt2pl_t pt2pl;
    render_params_pairings_pt2ln_t pt2ln;
};

/** @} */

}  // namespace mp2p_icp

MRPT_ENUM_TYPE_BEGIN(mp2p_icp::Coordinate)
MRPT_FILL_ENUM_MEMBER(mp2p_icp::Coordinate, X);
MRPT_FILL_ENUM_MEMBER(mp2p_icp::Coordinate, Y);
MRPT_FILL_ENUM_MEMBER(mp2p_icp::Coordinate, Z);
MRPT_ENUM_TYPE_END()
