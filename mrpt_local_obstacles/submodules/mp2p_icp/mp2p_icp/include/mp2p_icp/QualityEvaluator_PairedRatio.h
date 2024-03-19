/* -------------------------------------------------------------------------
 *  A repertory of multi primitive-to-primitive (MP2P) ICP algorithms in C++
 * Copyright (C) 2018-2021 Jose Luis Blanco, University of Almeria
 * See LICENSE for license information.
 * ------------------------------------------------------------------------- */
/**
 * @file   QualityEvaluator_PairedRatio.h
 * @brief  Matching quality evaluator: simple ratio [0,1] of paired entities.
 * @author Jose Luis Blanco Claraco
 * @date   July 6, 2020
 */
#pragma once

#include <mp2p_icp/Matcher_Points_DistanceThreshold.h>
#include <mp2p_icp/QualityEvaluator.h>

namespace mp2p_icp
{
/** Matching quality evaluator: simple ratio [0,1] of paired entities.
 *
 * \ingroup mp2p_icp_grp
 */
class QualityEvaluator_PairedRatio : public QualityEvaluator
{
    DEFINE_MRPT_OBJECT(QualityEvaluator_PairedRatio, mp2p_icp)

   public:
    /** See base class. Parameters:
     *
     * \code
     * thresholdDistance: 0.10
     * \endcode
     */
    void initialize(const mrpt::containers::yaml& params) override;

    double evaluate(
        const metric_map_t& pcGlobal, const metric_map_t& pcLocal,
        const mrpt::poses::CPose3D& localPose,
        const Pairings&             pairingsFromICP) const override;

   private:
    Matcher_Points_DistanceThreshold matcher_;
};

}  // namespace mp2p_icp
